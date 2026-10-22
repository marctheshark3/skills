#!/usr/bin/env python3
"""Offline schema, local-reference, and publication-gate checks; no installation."""

import copy
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError(f"Non-JSON numeric constant: {value}")


def read_json(path):
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_object,
        parse_constant=invalid_constant,
    )


def local_artifact(value):
    target = (ROOT / value.split("#", 1)[0]).resolve()
    if not target.is_relative_to(ROOT) or not target.exists():
        raise ValueError(f"Missing or escaping local artifact: {value}")
    return target


def check_local_references(catalog):
    entry_ids = set()
    for entry in catalog["entries"]:
        if entry["id"] in entry_ids:
            raise ValueError(f"Duplicate catalog id: {entry['id']}")
        entry_ids.add(entry["id"])
        for key in ("source", "recreation_brief"):
            if entry[key] is None:
                continue
            value = entry[key]["local_path"]
            if value is None:
                continue
            artifact = local_artifact(value)
            if key == "source" and not (artifact / "SKILL.md").is_file():
                raise ValueError(f"Source has no SKILL.md: {value}")
            if key == "recreation_brief" and not artifact.is_file():
                raise ValueError(f"Brief is not a file: {value}")
        evidence_ids = set()
        for evidence in entry["validation"]["evidence"]:
            if evidence["id"] in evidence_ids:
                raise ValueError(f"Duplicate evidence id: {evidence['id']}")
            evidence_ids.add(evidence["id"])
            if not local_artifact(evidence["report"]).is_file():
                raise ValueError(f"Evidence report is not a file: {evidence['report']}")


def check_mutations(validator, catalog, schema, public_catalog=None):
    """Evaluate data through the schema, rather than matching instruction text."""
    if not catalog["entries"]:
        raise ValueError("The review example must contain a prototype entry")
    if catalog["entries"][0]["publication_status"] != "unpublished-prototype":
        raise ValueError("These checks require the unpublished review example")
    count = 0

    def expect(label, candidate, valid=False):
        nonlocal count
        observed = validator.is_valid(candidate)
        if observed != valid:
            raise AssertionError(f"{label}: expected valid={valid}, observed {observed}")
        count += 1
        print(f"PASS {label}")

    def changed():
        candidate = copy.deepcopy(catalog)
        return candidate, candidate["entries"][0]

    candidate, entry = changed()
    entry["publication_status"] = "public"
    expect("public status alone cannot enable adoption", candidate)

    for option in ("download", "recreate_locally"):
        candidate, entry = changed()
        entry["adoption"][option]["available"] = True
        expect(f"unpublished {option} stays unavailable", candidate)

        candidate, entry = changed()
        entry["publication_status"] = "public"
        entry["adoption"][option]["available"] = True
        expect(f"public {option} needs provenance, license, and review", candidate)

    candidate, entry = changed()
    entry["source"]["local_path"] = "../outside"
    expect("source path traversal rejected", candidate)

    candidate, entry = changed()
    entry["recreation_brief"]["local_path"] = "/absolute/brief.txt"
    expect("absolute brief path rejected", candidate)

    candidate, entry = changed()
    entry["recreation_brief"]["version"] = "0.2.0-prototype"
    expect("brief version can evolve independently", candidate, valid=True)

    candidate, entry = changed()
    entry["recreation_brief"] = None
    expect("absent recreation brief is represented honestly", candidate, valid=True)

    candidate, entry = changed()
    entry["source"]["requirements"]["network"]["required"] = "conditional"
    expect("conditional network needs can be represented", candidate, valid=True)

    candidate, entry = changed()
    entry["recreation_brief"]["claim"] = "equivalent-to-source"
    expect("equivalence claim rejected", candidate)

    candidate, entry = changed()
    entry["validation"]["model_compatibility"]["status"] = "verified"
    expect("unsupported compatibility claim rejected", candidate)

    candidate, entry = changed()
    entry["unrecognized_install_command"] = "execute-me"
    expect("undeclared entry fields rejected", candidate)

    candidate, entry = changed()
    del entry["source"]["requirements"]["network"]
    expect("network requirements must be explicit", candidate)

    # Exercise distribution-review requirements separately without inventing a
    # public repository, artifact digest, license grant, or passed review record.
    for gate_index, label in ((2, "download"), (3, "recreation")):
        requirement = schema["$defs"]["entry"]["allOf"][gate_index]["then"]["properties"]["validation"]
        review_validator = validator.evolve(schema=requirement)
        if review_validator.is_valid(catalog["entries"][0]["validation"]):
            raise AssertionError(f"{label}: local checks must not qualify as distribution review")
        count += 1
        print(f"PASS {label} distribution review cannot be replaced by local checks")

    digest_validator = validator.evolve(schema=schema["$defs"]["sha256"])
    if digest_validator.is_valid("not-a-digest"):
        raise AssertionError("Malformed artifact digest accepted")
    count += 1
    print("PASS malformed artifact digest rejected")

    if public_catalog is not None:
        index = next((i for i, entry in enumerate(public_catalog["entries"])
                      if entry["adoption"]["download"]["available"]), None)
        if index is None:
            print("SKIP download-specific mutations: catalog has no available downloads")
            return count
        candidate = copy.deepcopy(public_catalog)
        candidate["entries"][index]["source"]["license"] = None
        expect("public download cannot lose its license", candidate)

        candidate = copy.deepcopy(public_catalog)
        candidate["entries"][index]["source"]["provenance"]["download_sha256"] = None
        expect("public download cannot lose its archive digest", candidate)

        candidate = copy.deepcopy(public_catalog)
        candidate["entries"][index]["adoption"]["recreate_locally"]["available"] = True
        expect("absent brief cannot become an available recreation option", candidate)
    return count


def main():
    schema = read_json(ROOT / "catalog.schema.json")
    catalog = read_json(ROOT / "catalog.example.json")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    catalogs = [("catalog.example.json", catalog)]
    public_catalog = read_json(ROOT / "catalog.json")
    catalogs.append(("catalog.json", public_catalog))
    for filename, data in catalogs:
        errors = sorted(validator.iter_errors(data), key=lambda error: str(list(error.path)))
        if errors:
            for error in errors:
                location = "/".join(map(str, error.path)) or "<root>"
                print(f"{filename}:{location}: {error.message}", file=sys.stderr)
            return 1
        check_local_references(data)
        print(f"PASS {filename}: schema agreement and local references ({len(data['entries'])} entries)")
    count = check_mutations(validator, catalog, schema, public_catalog)
    print(f"PASS {count} publication and contract checks")
    print("Public access, license rights, and agent behavior are not established by these checks.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, KeyError, OSError, ValueError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        sys.exit(1)

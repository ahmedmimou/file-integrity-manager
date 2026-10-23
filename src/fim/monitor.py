
def compare_scans(
        current_scan:  list[dict[str, str]],
        baseline : dict[str, str],
) -> dict[str, list[str]]:
    current ={
        item["path"]: item["sha256"]
        for item in current_scan
    }

    unchanged = []
    modified = []
    new = []
    deleted = []

    for path, current_hash in current.items():
        if path not in baseline:
            new.append(path)
        elif current_hash != baseline[path]:
            modified.append(path)
        else:
            unchanged.append(path)

    for path in baseline:
        if path not in current:
            deleted.append(path)

    return{
        "unchanged": unchanged,
        "modified": modified,
        "new": new,
        "deleted": deleted,
    }
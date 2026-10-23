from src.fim.monitor import compare_scans



def test_unchanged_files():
    current_scan = [
        {"path": "a.txt", "sha256": "hash123"}
    ]
    baseline = {
        "a.txt": "hash123"
    }

    result = compare_scans(current_scan, baseline)

    assert result["unchanged"] == ["a.txt"]
    assert result["modified"] == []
    assert result["new"] == []
    assert result["deleted"] == []


def test_modified_files():
    current_scan = [
        {"path": "a.txt", "sha256": "new_hash"}
    ]
    baseline = {
        "a.txt": "old_hash"
    }

    result = compare_scans(current_scan, baseline)

    assert result["modified"] == ["a.txt"]

def test_new_files():
    current_scan = [
        {"path": "new.txt", "sha256": "hash123"}
    ]
    baseline = {}

    result = compare_scans (current_scan, baseline)

    assert result["new"] == ["new.txt"]

def test_deleted_file():
    current_scan = []
    baseline = {"old.txt": "hash123"} 

    result = compare_scans(current_scan , baseline)
    assert result["deleted"] == ["old.txt"]

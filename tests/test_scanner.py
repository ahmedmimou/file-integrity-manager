from src.fim.scanner import scan_directory


def test_scan_directory_finds_files(tmp_path):
    root = tmp_path / "documents"
    subfolder = root / "projects"

    subfolder.mkdir(parents = True)
    (root / "report.txt").write_text("Report", encoding = "utf-8")
    (subfolder / "main.py").write_text("print('Hello')", encoding = "utf-8")

    results = scan_directory(str(root))

    paths = {item["path"] for item in results}

    assert len(results) == 2
    assert any(path.endswith("report.txt") for path in paths)
    assert any(path.endswith("main.py") for path in paths)

def test_scan_empty_directory_returns_empty_list(tmp_path):
    root = tmp_path / "empty"
    root.mkdir()

    results = scan_directory(str(root))

    assert results == []
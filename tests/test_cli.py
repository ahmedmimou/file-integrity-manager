
import pytest

from fim.cli import main


def test_scan_nonexistent_directory(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["fim", "scan", "folder_that_does_not_exist"],
    )

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2

    captured = capsys.readouterr()
    assert "Directory does not exist" in captured.err


def test_scan_file_instead_of_directory(tmp_path, monkeypatch, capsys):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello", encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        ["fim", "scan", str(file_path)],
    )

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2

    captured = capsys.readouterr()
    assert "Path is not a directory" in captured.err

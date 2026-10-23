from src.fim.hashing import calculate_sha256


def test_calculate_sha256(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Hello World", encoding="utf-8")

    result = calculate_sha256(test_file)

    assert result == (
        "a591a6d40bf420404a011733cfb7b190"
        "d62c65bf0bcda32b57b277d9ad9f146e"
    )

def test_hash_changes_when_content_changes(tmp_path):
    test_file = tmp_path / "sample.txt"

    test_file.write_text("Hello World", encoding = "utf-8")
    original_hash = calculate_sha256(test_file)
    
    test_file.write_text("Hello FIM", encoding = "utf-8")
    modified_hash = calculate_sha256(test_file)

    assert original_hash != modified_hash

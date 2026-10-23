import hashlib


def calculate_sha256(file_path: str) -> str:
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(65536)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()
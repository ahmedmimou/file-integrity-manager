from pathlib import Path
from src.fim.hashing import calculate_sha256

def scan_directory(directory: str) -> list[dict[str, str]]:
    root = Path(directory)
    results = []

    
    for item in root.rglob("*"):
        if item.is_file():
            file_hash = calculate_sha256(str(item))
            results.append({
                "path" : str(item),
                "sha256" : file_hash
            })
    return results
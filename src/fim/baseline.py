import json
from pathlib import Path

def save_baseline(
        scan_results: list[dict[str , str]],
        baseline_path: str,
) -> None:
    baseline = {
        item["path"]: item["sha256"]
        for item in scan_results
    }
    with open(baseline_path , "w" ,encoding = "utf-8")as file:
        json.dump(baseline, file, indent=4)

def load_baseline(baseline_path: str) -> dict[str, str]:
    with open(baseline_path, "r" ,  encoding = "utf-8") as file:
        return json.load(file)

# File Integrity Manager

A Python tool that monitors file integrity using SHA-256 hashing.

File Integrity Manager scans files in a directory, calculates their SHA-256 hashes, saves a baseline of the original file states, and detects changes during subsequent scans.

## Features

- **SHA-256 Hashing:** Calculates file hashes to identify content changes.
- **Directory Scanning:** Recursively scans files in a directory and its subdirectories.
- **Baseline Management:** Saves and loads file hashes using JSON.
- **Change Detection:** Identifies unchanged, modified, new, and deleted files.
- **Command-Line Interface:** Provides simple commands to scan, create a baseline, and check for changes.
- **Automated Tests:** Includes tests using pytest.


## Requirements

- Python 3.10 or later
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ahmedmimou/file-integrity-manager.git
cd file-integrity-manager
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install the project

```bash
python -m pip install -e .
```

## Usage

Run commands from the project root directory.

### Scan a directory

Calculate and display SHA-256 hashes for files:

```bash
python -m fim.cli scan demo
```

### Create a baseline

Save the current file hashes to `baseline.json`:

```bash
python -m fim.cli baseline demo
```

### Check for changes

Compare the current directory state with the saved baseline:

```bash
python -m fim.cli check demo
```

The check command reports files as:

- **Unchanged:** Files whose hashes match the baseline.
- **Modified:** Files whose hashes have changed.
- **New:** Files that were not present in the baseline.
- **Deleted:** Files that were present in the baseline but are now missing.

## Running Tests

The project uses `pytest` for automated testing.

Run the test suite from the project root:

```bash
python -m pytest -v
```

The tests cover:

- SHA-256 hash calculation.
- Recursive directory scanning.
- Detection of unchanged, modified, new, and deleted files.
- Command-line error handling.

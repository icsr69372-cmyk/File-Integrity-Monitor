# File Integrity Monitoring System

## Project Overview

File Integrity Monitoring System is a Python-based
cybersecurity project that monitors files and detects
unauthorized changes using SHA-256 hashing.

## Features

- Calculate SHA-256 hashes for files.
- Detect modified files.
- Detect deleted files.
- Automatically detect new files.
- Store original file hashes using JSON.
- Record security events with date and time.
- Generate security reports.
- Display overall security status (SAFE / ALERT).

## Technologies Used

- Python
- hashlib: For SHA-256 hashing.
- os: For file and directory operations.
- json: For storing file hashes.
- datetime: For recording date and time.

## Project Structure

File_Integrity_Monitor/
│
├── main.py
├── hash_record.json
├── monitor_log.txt
├── README.md
├── test.txt
├── notes.txt
└── important.txt

## How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py


## Example Output

```text
Original hashes loaded successfully.

notes.txt WARNING! File has been modified.
photo.txtt is SAFE. No changes detected.
text.txt WARNING! File has been modified.
important.txt WARNING! File has been deleted.

========== SECURITY REPORT ==========
Total Files Scanned: 4
New Files: 0
Modified Files: 2
Deleted Files: 1
Safe Files: 1
Security Status: ALERT
=====================================


This project helped me practice:

- Python programming.
- File handling.
- Dictionaries and Lists.
- Functions and loops.
- SHA-256 hashing.
- Basic file integrity monitoring.
- Cybersecurity fundamentals.
import hashlib
import os
import json

from datetime import datetime

record_path = "hash_record.json"

excluded_files = [
    "main.py",
    "README.md",
    ".gitignore",
    "hash_record.json",
    "hash_record.txt",
    "monitor_log.txt"
]


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        content = file.read()

    sha256.update(content)

    return sha256.hexdigest()


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("monitor_log.txt","a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    
# Get all files automatically
all_items = os.listdir(".")

files_to_monitor = []

for item in all_items:
    if os.path.isfile(item) and item not in excluded_files:
        files_to_monitor.append(item)


# Calculate hashes
file_hashes = {}

for file in files_to_monitor:
    file_hashes[file] = calculate_hash(file)


# Save or compare hashes
if not os.path.exists(record_path):

    with open(record_path, "w") as file:
        json.dump(file_hashes, file, indent=4)

    print("Original hashes saved successfully.")

else:

    with open(record_path, "r") as file:
        saved_hashes = json.load(file)

    print("Original hashes loaded successfully.")

    new_file_added = False

    new_files_count = 0
    modified_files_count=0
    deleted_files_count=0
    safe_files_count=0


    # Detect new, modified and safe files
    for file in files_to_monitor:

        if file not in saved_hashes:
            print(file, "is a NEW file.")
            log_event(f"{file} is a new file")
            new_files_count+=1

            saved_hashes[file] = file_hashes[file]
            new_file_added = True

        elif saved_hashes[file] != file_hashes[file]:
            print(file, "WARNING! File has been modified.")
            log_event(f"{file} was modified")
            modified_files_count+=1

        else:
            print(file, "is SAFE. No changes detected.")
            safe_files_count +=1

    # Detect deleted files
    for saved_file in saved_hashes:

        if saved_file not in files_to_monitor:
            print(saved_file, "WARNING! File has been deleted.")
            log_event(f"{saved_file} was deleted")
            deleted_files_count+=1

    # Save new files only
    if new_file_added:

        with open(record_path, "w") as file:
            json.dump(saved_hashes, file, indent=4)

        print("New file hashes saved successfully.")

    print("\n========== SECURITY REPORT ==========")

    print(f"New Files: {new_files_count}")
    print(f"Modified Files: {modified_files_count}")
    print(f"Deleted Files: {deleted_files_count}")
    print(f"safe files:{safe_files_count}")
    print(f"total files scanned:{len(files_to_monitor)}")

    if modified_files_count > 0 or deleted_files_count > 0 or new_files_count > 0:
     print("Security Status: ALERT")

    else:
     print("Security Status: SAFE")

    if modified_files_count > 0 or deleted_files_count > 0 or new_files_count > 0:
     print("Security Status: ALERT")

    else:
      print("Security Status: SAFE")  

    print("=====================================")

    log_event(
    f"Scan completed | New: {new_files_count} | "
    f"Modified: {modified_files_count} | "
    f"Deleted: {deleted_files_count}"
)
import schedule
import time
import shutil
import os
from datetime import datetime

def backup_file(source_file, destination_dir):
    try:
        filename, extension = os.path.splitext(os.path.basename(source_file))

        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        backup_filename = f"{filename}_{timestamp}{extension}"

        destination_path = os.path.join(destination_dir, backup_filename)

        shutil.copy2(source_file, destination_path)

        log_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        with open("backup_log.txt", "a") as log_file:
            log_file.write(
                f"Backup completed successfully at {log_time}\n"
            )

        print("Backup completed successfully.")

    except Exception as e:
        print("Error:", e)

def main():
    source_file = input("Enter source file path: ")
    destination_dir = input("Enter destination directory path: ")

    schedule.every(1).hours.do(
        backup_file,
        source_file=source_file,
        destination_dir=destination_dir
    )

    print("Backup scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
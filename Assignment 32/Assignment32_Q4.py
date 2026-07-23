import os
import shutil
import time
from datetime import datetime

LOG_FILE = "CopyLog.txt"


def copy_txt_files(source_dir, destination_dir):
    try:
        with open(LOG_FILE, "a") as log:

            for filename in os.listdir(source_dir):

                if filename.endswith(".txt"):
                    source_file = os.path.join(source_dir, filename)
                    destination_file = os.path.join(destination_dir, filename)

                    try:
                        shutil.copy2(source_file, destination_file)

                        message = (
                            f"{datetime.now()} - COPIED: "
                            f"{source_file} -> {destination_file}\n"
                        )

                        log.write(message)
                        print(message.strip())

                    except Exception as e:
                        error_message = (
                            f"{datetime.now()} - FAILED: "
                            f"{source_file} - {e}\n"
                        )

                        log.write(error_message)
                        print(error_message.strip())

    except Exception as e:
        print(f"Logging Error: {e}")


def main():
    source_dir = input("Enter source directory: ")
    destination_dir = input("Enter destination directory: ")

    if not os.path.isdir(source_dir):
        print("Invalid source directory.")
        return

    if not os.path.isdir(destination_dir):
        print("Invalid destination directory.")
        return

    while True:
        copy_txt_files(source_dir, destination_dir)
        print("Waiting 10 minutes for next execution...\n")
        time.sleep(600)  # 10 minutes


if __name__ == "__main__":
    main()
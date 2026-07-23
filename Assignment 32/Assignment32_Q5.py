import os
import time
from datetime import datetime

LOG_FILE = "DeletedFilesLog.txt"


def delete_empty_files(directory):
    try:
        with open(LOG_FILE, "a") as log:

            for root, dirs, files in os.walk(directory):

                for file in files:
                    file_path = os.path.join(root, file)

                    try:
                        # Check if file is empty
                        if os.path.getsize(file_path) == 0:

                            os.remove(file_path)

                            message = (
                                f"{datetime.now()} - DELETED: {file_path}\n"
                            )

                            log.write(message)
                            print(message.strip())

                    except PermissionError:
                        error_message = (
                            f"{datetime.now()} - PERMISSION DENIED: {file_path}\n"
                        )

                        log.write(error_message)
                        print(error_message.strip())

                    except FileNotFoundError:
                        error_message = (
                            f"{datetime.now()} - FILE NOT FOUND: {file_path}\n"
                        )

                        log.write(error_message)
                        print(error_message.strip())

                    except OSError as e:
                        error_message = (
                            f"{datetime.now()} - ERROR: {file_path} - {e}\n"
                        )

                        log.write(error_message)
                        print(error_message.strip())

    except Exception as e:
        print(f"Logging Error: {e}")


def main():
    directory = input("Enter directory path: ")

    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    while True:
        print("\nScanning for empty files...")
        delete_empty_files(directory)

        print("Waiting 1 hour for next scan...\n")
        time.sleep(3600)  # 1 hour


if __name__ == "__main__":
    main()
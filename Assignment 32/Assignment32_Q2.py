import os
import time
from datetime import datetime

FILE_TO_MONITOR = "sample.txt"   # Change to your file name
LOG_FILE = "FileSizeLog.txt"


def log_file_size():
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(LOG_FILE, "a") as log:
        if os.path.exists(FILE_TO_MONITOR):
            size = os.path.getsize(FILE_TO_MONITOR)

            log.write(
                f"File Path: {os.path.abspath(FILE_TO_MONITOR)}, "
                f"File Size: {size} bytes, "
                f"Date & Time: {current_time}\n"
            )

            print(f"Logged size: {size} bytes")
        else:
            log.write(
                f"File Path: {os.path.abspath(FILE_TO_MONITOR)}, "
                f"File does not exist, "
                f"Date & Time: {current_time}\n"
            )

            print("File does not exist")


def main():
    while True:
        log_file_size()
        time.sleep(30)  # Wait 30 seconds


if __name__ == "__main__":
    main()
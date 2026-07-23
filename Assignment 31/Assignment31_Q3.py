import os
import schedule
import time
from datetime import datetime

def scan_directory(directory):
    try:
        files = 0
        subdirectories = 0

        for item in os.listdir(directory):
            path = os.path.join(directory, item)

            if os.path.isfile(path):
                files += 1
            elif os.path.isdir(path):
                subdirectories += 1

        scan_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        print("\nDirectory Scanned:", directory)
        print("Total Files:", files)
        print("Total Subdirectories:", subdirectories)
        print("Scan Time:", scan_time)

    except FileNotFoundError:
        print("Directory does not exist.")

def main():
    directory = input("Enter directory path: ")

    # Scan every minute
    schedule.every(1).minutes.do(scan_directory, directory)

    # Optional: Perform first scan immediately
    scan_directory(directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
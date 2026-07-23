import os
import schedule
import time
from datetime import datetime

def count_files(directory):
    try:
        file_count = 0

        for item in os.listdir(directory):
            path = os.path.join(directory, item)

            if os.path.isfile(path):
                file_count += 1

        current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        with open("DirectoryCountLog.txt", "a") as file:
            file.write(f"Directory Path : {directory}\n")
            file.write(f"Number of Files: {file_count}\n")
            file.write(f"Date and Time : {current_time}\n")
            file.write("-" * 40 + "\n")

        print("Log entry added successfully.")

    except FileNotFoundError:
        print("Directory not found.")

def main():
    directory = input("Enter directory path: ")

    count_files(directory)  # Optional: perform first scan immediately

    schedule.every(5).minutes.do(count_files, directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
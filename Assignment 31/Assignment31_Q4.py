import schedule
import time
from datetime import datetime

def create_log_file():
    current_time = datetime.now()

    filename = "MarvellousLog_" + current_time.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Log file created successfully.\n")
        file.write("Creation Time: " +
                   current_time.strftime("%d-%m-%Y %I:%M:%S %p"))

    print(f"{filename} created successfully.")

def main():
    create_log_file()  # Optional: create first file immediately

    schedule.every(10).minutes.do(create_log_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
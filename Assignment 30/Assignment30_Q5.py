import schedule
import time
from datetime import datetime

def write_to_file():
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("Marvelous.txt", "a") as file:
        file.write(f"Task executed at: {current_time}\n")

    print("Date and time appended successfully.")

def main():
    schedule.every(5).minutes.do(write_to_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
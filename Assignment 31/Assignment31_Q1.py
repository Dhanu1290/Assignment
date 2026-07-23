import schedule
import time

def display_message(message):
    print(message)

def main():
    message = input("Enter message: ")
    interval = int(input("Enter interval in seconds: "))

    if interval <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(interval).seconds.do(display_message, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
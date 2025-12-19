from datetime import datetime
import csv
import os

FILENAME = "weather_log.csv"

# ---------- CLASS ----------
class WeatherEntry:
    def __init__(self, date_time, temperature, humidity):
        self.date_time = date_time
        self.temperature = temperature
        self.humidity = humidity

    def to_list(self):
        return [self.date_time, self.temperature, self.humidity]


# ---------- VALIDATION ----------
def validate_temperature(temp):
    return -50 <= temp <= 60

def validate_humidity(hum):
    return 0 <= hum <= 100


# ---------- FILE HANDLING ----------
def log_weather(temp, humidity):
    if not validate_temperature(temp):
        print("Invalid temperature!")
        return

    if not validate_humidity(humidity):
        print("Invalid humidity!")
        return

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = WeatherEntry(date_time, temp, humidity)

    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["DateTime", "Temperature", "Humidity"])
        writer.writerow(entry.to_list())

    print(f"Logged: {date_time}, {temp}, {humidity}")


def read_logs():
    if not os.path.isfile(FILENAME):
        print("No weather data found.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)


# ---------- MENU ----------
def main():
    while True:
        print("\nDaily Weather Logging System")
        print("1. Log Weather Data")
        print("2. View Weather Logs")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                temp = float(input("Enter Temperature (°C): "))
                humidity = float(input("Enter Humidity (%): "))
                log_weather(temp, humidity)
            except ValueError:
                print("Please enter numeric values.")

        elif choice == "2":
            read_logs()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

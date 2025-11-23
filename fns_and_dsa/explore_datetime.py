from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and time: {formatted_datetime}")

    return current_date

if __name__ == "__main__":
    display_current_datetime()

from datetime import datetime, timedelta
def display_current_datetime():
    
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and time: {formatted_datetime}")
    return current_date

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)

    formatted_future_date = future_date.strftime("%Y-%M-%d")
    print(f"Future Date: {formatted_future_date}")
    return future_date

if __name__ == "__main__":
    print("Calculate a future date ===")
    calculate_future_date()
        
    
from datetime import datetime ,timedelta
current_date = datetime.now()

def display_current_datetime():
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
display_current_datetime()

def calculate_future_date():
    numbers_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days = numbers_of_days)
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))
calculate_future_date()

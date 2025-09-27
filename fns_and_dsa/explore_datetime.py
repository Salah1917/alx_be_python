from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)

def calculate_future_date(num_of_days):
    ini_time_for_now = datetime.now()
    
    future_date = ini_time_for_now + timedelta(days = num_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    
display_current_datetime()

num_of_days = int(input(("Enter the number of days to add to the current date: ")))

calculate_future_date(num_of_days)

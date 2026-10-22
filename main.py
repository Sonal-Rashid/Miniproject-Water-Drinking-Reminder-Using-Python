import time
from plyer import notification

def drink_water_reminder(interval_minutes):
    if interval_minutes <= 0:
        print("Invalid input: Please enter an interval greater than 0.")
        return
    
    interval_seconds = interval_minutes * 60
    # interval_seconds = interval_minutes # testing interval
    
    print(f"Water reminder started: You will be notified every {interval_minutes} minutes")

    print("Press Ctrl + C to stop the reminder.")

    while True:
        time.sleep(interval_seconds)
        notification.notify(
            title="Water Reminder", 
            message="It is time to drink water",
            timeout = 10
        )

drink_water_reminder(60)
# drink_water_reminder(5) # testing interval

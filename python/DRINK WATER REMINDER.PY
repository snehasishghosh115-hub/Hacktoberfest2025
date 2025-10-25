import time
from plyer import notification

def water_reminder(interval_minutes):
    """
    Function to remind the user to drink water every 'interval_minutes' minutes
    :param interval_minutes: Number of minutes between reminders
    """
    try:
        while True:
            # Show desktop notification
            notification.notify(
                title="💧 Time to Drink Water!",
                message=f"Stay hydrated! Drink a glass of water now.",
                timeout=10  # Notification stays for 10 seconds
            )
            # Wait for the specified interval before the next reminder
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("
Reminder stopped. Stay hydrated!")

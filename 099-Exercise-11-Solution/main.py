# Exercise 11 - Solution

from plyer import notification
import time

def notify():
    notification.notify(
        title='Drink Water Reminder',
        message="It's time for drinking another glass of water",
        app_name='Reminder from Python',
        timeout=10
    )

while(True):
    notify()
    time.sleep(3600)
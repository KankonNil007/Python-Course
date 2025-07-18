# Reminder App

from plyer import notification
import time

print("====== Water Reminder App ======")

inpMsg = input("Enter Reminder Message: ")
inpTime = int(input("Enter the Interval(in seconds): "))

def notify():
    notification.notify(
        title='Reminder',
        message=f"{inpMsg}",
        app_name='Reminder from Python',
        timeout=5
    )

while(True):
    notify()
    time.sleep(inpTime)

# Note: It is an infinte loop, if your PC keep showing notification even after closing the terminal , then go to the task manager and end task of python.
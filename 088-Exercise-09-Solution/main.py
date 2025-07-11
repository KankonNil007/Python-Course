# Exercise 09 - Solution

import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")

list1 = ["Kankon", "Harry", "Shovon", "Pain"]

for i in list1:
    speak.Speak(f"Shoutout to {i}")
    time.sleep(1)
# Exercise 09 - Shoutouts to Everyone

import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")

list1 = ["Kankon", "Harry", "Shovon"]

for i in list1:
    speak.Speak(f"Shoutout to {i}")
    time.sleep(1)
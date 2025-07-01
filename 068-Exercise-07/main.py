# Exercise 07

import os

imageList = os.listdir("068-Exercise-07/images")
imageList.sort()

for index, i in enumerate(imageList, start=1):
    os.rename(f"068-Exercise-07/images/{i}", f"068-Exercise-07/images/photo_{index}.jpeg")
# Exercise 07 - Solution

import os

imageList = os.listdir("075-Exercise-07-Solution/images")
imageList.sort()

for index, i in enumerate(imageList, start=1):
    if i.endswith(".jpeg"):
        os.rename(f"075-Exercise-07-Solution/images/{i}", f"075-Exercise-07-Solution/images/photo_{index}.jpeg")
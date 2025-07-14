# AsyncIO in Python

# AsyncIO is such a method that does multitasking. Suppose we have 3 functions. But we have to run it one by one. But using asyncIO, we can multitask the functions

import asyncio
import requests

async def function1():
    print("func 1")
    URL = "https://t4.ftcdn.net/jpg/04/39/89/01/360_F_439890152_sYbPxa1ANTSKcZuUsKzRAf9O7bJ1Tx5B.jpg"
    response = requests.get(URL)
    open("096-AsyncIO-in-Python/img1.jpg", "wb").write(response.content)

async def function2():
    print("func 2")
    URL = "https://t4.ftcdn.net/jpg/04/39/89/01/360_F_439890152_sYbPxa1ANTSKcZuUsKzRAf9O7bJ1Tx5B.jpg"
    response = requests.get(URL)
    open("096-AsyncIO-in-Python/img2.jpg", "wb").write(response.content)

async def function3():
    print("func 3")
    URL = "https://t4.ftcdn.net/jpg/04/39/89/01/360_F_439890152_sYbPxa1ANTSKcZuUsKzRAf9O7bJ1Tx5B.jpg"
    response = requests.get(URL)
    open("096-AsyncIO-in-Python/img3.jpg", "wb").write(response.content)

async def main():
    # Running them In Order or Series
    # await function1()
    # await function2()
    # await function3()

    # Running them Parallelly
    await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

asyncio.run(main())
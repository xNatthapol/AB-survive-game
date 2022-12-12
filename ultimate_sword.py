import turtle
import time

screen = turtle.Screen()
screen.setup(1280,720)
screen.title("-  Ultimate Sword  -")
for i in range(1,154,4):
    if i < 10:
        screen.bgpic(f"sword/sword-0000{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)
    elif i < 100:
        screen.bgpic(f"sword/sword-000{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)
    elif i < 1000:
        screen.bgpic(f"sword/sword-00{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)

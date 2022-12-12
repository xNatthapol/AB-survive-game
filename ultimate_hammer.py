import turtle
import time

screen = turtle.Screen()
screen.setup(1280,720)
screen.title("-  Ultimate Hammer  -")
for i in range(1,158,4):
    if i < 10:
        screen.bgpic(f"hammer/hammer-0000{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)
    elif i < 100:
        screen.bgpic(f"hammer/hammer-000{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)
    elif i < 1000:
        if i == 157:
            screen.bgpic(f"hammer/hammer-00{str(i)}.png")
            screen.bgcolor("white")
            time.sleep(0.1)
        else:
            screen.bgpic(f"hammer/hammer-00{str(i)}.png")
            screen.bgcolor("white")
            time.sleep(0.001)
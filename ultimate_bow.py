import turtle
import time

screen = turtle.Screen()
screen.setup(1280,720)
screen.title("-  Ultimate Bow  -")
for i in range(1,138,4):
    if i < 10:
        screen.bgpic(f"bow/bow-0000{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)
    elif i < 100:
        screen.bgpic(f"bow/bow-000{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)
    elif i < 1000:
        screen.bgpic(f"bow/bow-00{str(i)}.png")
        screen.bgcolor("white")
        time.sleep(0.001)

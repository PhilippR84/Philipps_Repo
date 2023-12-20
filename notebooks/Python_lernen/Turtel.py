import turtle
box = turtle.Turtle()
box.speed(4)

box.forward(200)
box.left(90)
box.forward(200)
box.left(90)
box.forward(200)
box.right(135)
box.forward(282.843/2)
box.right(90)
box.forward(282.843/2)
box.right(90)
box.forward(282.843)
box.right(135)
box.forward(200)
box.right(135)
box.forward(282.843)

turtle.exitonclick()
turtle.done
"""

import turtle
#Inside_Out
wn = turtle. Screen()
wn.bgcolor ("light green")
skk = turtle. Turtle()
skk.color ("blue")

size = 6
for i in range(10):
    for i in range(4):
        skk.forward(size)
        skk.left(90)
        size = size + 5


def sarfunc(size):
    for i in range (4):
        skk.fd(size)
        skk. left (90)
        size = size + 5

sarfunc (6)
sarfunc (26)	
sarfunc (46)	
sarfunc (66)	
sarfunc (86)	
sarfunc (106)	
sarfunc (126)	
sarfunc (146)
"""
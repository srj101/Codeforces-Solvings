import turtle
colors = ["red", "purple", "green", "orange", "blue", "pink"]
t = turtle.Pen()

turtle.bgcolor("white")

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

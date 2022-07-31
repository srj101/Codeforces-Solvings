import turtle
colors = ["yellow", "white", "green",
          "orange", "blue", "red", "pink", "purple"]
t = turtle.Pen()

turtle.bgcolor("black")

for x in range(360):
    t.pencolor(colors[x % 8])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

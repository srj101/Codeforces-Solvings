import turtle


t = turtle.Turtle()

# input for number of sides
n_sides = 12


for _ in range(n_sides):
    angle = 360/n_sides
    turtle.fd(100)
    turtle.rt(angle)

turtle.done()

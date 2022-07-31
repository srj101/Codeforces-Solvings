from operator import le
import turtle
flower = turtle.Turtle()
flower.speed(0)


def flowerr():
    for i in range(300):
        flower.circle(190-i, 90)
        flower.left(90)
        flower.circle(190-i, 90)
        flower.left(18)


flowerr()
flower.mainloop()

import turtle

t = turtle.Pen()
turtle.bgcolor('black')
t.turtlesize(2)
t.begin_fill()


COLOR_COUNT = 6

for x in range(400):
    if x % COLOR_COUNT == 0:
        t.pencolor("red")
    elif x % COLOR_COUNT == 1:
        t.pencolor("purple")
    elif x % COLOR_COUNT == 2:
        t.pencolor("blue")
    elif x % COLOR_COUNT == 3:
        t.pencolor("green")
    elif x % COLOR_COUNT == 4:
        t.pencolor("orange")
    elif x % COLOR_COUNT == 5:
        t.pencolor("yellow")

    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)
    t.right(10)
    t.showturtle()
    t.shape('turtle')


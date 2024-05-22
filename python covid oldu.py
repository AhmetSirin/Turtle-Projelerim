import turtle

a = 0
b = 0

turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a = a+3
    b = b+1
    if b==200:
        break
turtle.hideturtle()
turtle.exitonclick()

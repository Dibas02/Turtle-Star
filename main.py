import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)

turtle = turtle.Turtle()

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.pendown()
for j in range(3):
    turtle.forward(100)
    turtle.right(120)

turtle.mainloop()
turtle.done()
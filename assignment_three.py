import turtle
turtle.speed(10)

def side_length():
    length = input("What is the length of the cross?")
    return float(length)


def fill_color():
    fill_color = input("What color is the cross?")
    return fill_color


def draw_a_cross(side):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)


draw_a_cross(100)

turtle.exitonclick()


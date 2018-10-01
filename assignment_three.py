import turtle


def side_length():
    side = input("What is the length of the cross?")
    return float(side)


def fill_color():
    color = input("What color is the cross?")
    return color


def draw_a_cross(side, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.end_fill()


def move(x,y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down


def main():
    length = side_length()
    color = fill_color()
    draw_a_cross(length, color)
    turtle.up()
    move(2 * length, -2 * length)
    turtle.down
    draw_a_cross(length, color)
    move(0, 0)
    turtle.backward(length)
    draw_a_cross(length, color)
    move(0, 0)
    move(-length, -length * 2)
    turtle.backward(length)
    draw_a_cross(length, color)


    turtle.exitonclick()


main()

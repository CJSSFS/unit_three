import turtle


def side_length():
    """
    This function gets the side length from the user
    :return:
    """
    side = input("What is the length of the cross?")
    return float(side)


def fill_color():
    """
    This function gets the fill color from the user
    :return:
    """
    color = input("What color is the cross?")
    return color


def draw_a_cross(side, color):
    """
    This function tells turtle the steps to draw a cross
    :param side:
    :param color:
    :return:
    """
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
    """
    This tells the main function to tell the turtle to go to the next set position
    :param x:
    :param y:
    :return:
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down


def main():
    turtle.speed(30)
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
    move(0, 0)
    turtle.right(90)
    turtle.forward(length * 3)
    turtle.left(90)
    draw_a_cross(length, color)



    turtle.exitonclick()


main()

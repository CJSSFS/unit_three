import turtle



def side_length():
    side = input("What is the length of the cross?")
    return float(side)


def fill_color():
     color = input("What color is the cross?")
    turtle.begin_fill
    return fill_color


def draw_a_cross(side, color):
    for x in range(2):
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

def move(x,y):
    turtle.up()

def main():
    length = side_length()
    draw_a_cross(length)

    turtle.exitonclick()

main()
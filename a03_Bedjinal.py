

# TODO Do not edit this file directly! Instead, create a new file called
# TODO a03_username.py and copy this code into it!

#################################################################################
# Author:Bedjinal
# Username:Bedji05
#
# Assignment:A03
# Purpose:Learn
# Google Doc Link:https://docs.google.com/document/d/1sHCBymctx6N0hP3KoowlDGdShjClpZRaNIBIFWgG_KA/edit#
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def make_window(Bed):         # to draw the small window
    """
    Docstring for function_1
    """
    for i in range(4):
        Bed.fd(130)
        Bed.left(90)
    Bed.fd(65)
    Bed.left(90)
    Bed.fd(130)


    # ....


def make_house(Bed2):      #to draw the square, whivh the body of the house
    """
    Docstring for function_2
    """
    Bed2.pensize(10)
    tup = (0.4, 0.8, 0.75)
    Bed2.pencolor(tup)

    Bed2.penup()
    Bed2.setposition(-200, -200)
    Bed2.pendown()
    for i in range(4):
        Bed2.fd(400)
        Bed2.left(90)

    # ...
def make_roof(Bed3):                                # to draw the roof

    """
    Docstring for function_3
    """
    Bed3.penup()
    Bed3.pensize(10)
    Bed3.setposition(-200, 200)
    Bed3.pendown()
    Bed3.left(30)
    Bed3.fd(235)
    Bed3.right(60)
    Bed3.fd(220)
   # Bed3.fillcolor(0.7, .5, 0.65)

def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()  # creates a graphics window
    wn.bgcolor('green')
    Bed = turtle.Turtle()
    Bed2 = turtle.Turtle()
    Bed.pensize(10)
    Bed.color('red')
    Bed3 = turtle.Turtle()



    # ...
    make_window(Bed)            # Function call to function_1
    make_house(Bed2)            # Function call to function_2
    make_roof(Bed3)             # Function call to function_3
    wn.exitonclick()
main()



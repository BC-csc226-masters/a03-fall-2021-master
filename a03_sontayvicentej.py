#############################
#Author: Jhonny Sontay-Vicente
#Username:Sontayvicentej
#Assignment:a03
#googledoc link: https://docs.google.com/document/d/1qhuiJAg5e30WXqbCY4657AIk2IeKXb2JWs4butPLulE/edit?usp=sharing

##############################\

#Acknowledgements: https://docs.python.org/3.0/library/turtle.html

###############################

import turtle

def new_building(turt,length,height):
    """tells turtle to drawbuilding of height and length"""
    turt.seth(0)
    for i in range(2):
        turt.fd(length)
        turt.left(90)
        turt.fd(height)
        turt.left(90)

def move_it(turt,x,y):
    """Moves turtle to a coordinate"""
    turt.seth(0)
    turt.penup()
    turt.setpos(x,y)
    turt.pendown()
def construct_window(turt,length):
    """uses turtle to make a window"""
    turt.seth(0)
    for i in range(4):
        turt.fd(length)
        turt.left(90)
    turt.fd(length/2)
    turt.left(90)
    turt.fd(90)
    turt.right(90)
    turt.fd(length/2)
    turt.right(90)
    turt.fd(length / 2)
    turt.right(90)
    turt.fd(90)
def many_windows(turt,x,y):
    """makes many windows"""
    turt.seth(0)
    move_it(turt, x, y)
    construct_window(turt, 90)
    move_it(turt, x + 135, y)
    construct_window(turt, 90)
    move_it(turt, x+270, y)
    construct_window(turt, 90)
def make_door(turt,x,y,length,height):
    """tells turtle to make a door"""
    turt.seth(0)
    move_it(turt,x,y)
    turt.fillcolor("white")
    turt.begin_fill()
    turt.fd(length)
    for i in range(2):
        turt.fd(length)
        turt.left(90)
        turt.fd(height)
        turt.left(90)
    turt.end_fill()
    turt.penup()
    turt.setpos(x+(length*1.5),y+(height/2))
    turt.pendown()
    turt.dot(20, "gold")


def main():
    wn = turtle.Screen()

    wn.bgcolor("orange")

    raphael = turtle.Turtle()
    raphael.ht()
    raphael.speed(0)
    raphael.pensize(5)
    move_it(raphael,-250,-250)
    raphael.pencolor("yellow")
    raphael.color("yellow")
    new_building(raphael,450,500)   #makes the building
    many_windows(raphael,-205,155)   #makes windows
    many_windows(raphael,-205,55)    #makes windows
    many_windows(raphael,-205,-55)    #makes windows
    make_door(raphael,-140,-250,80,120)  #makes door
    wn.exitonclick()
main()
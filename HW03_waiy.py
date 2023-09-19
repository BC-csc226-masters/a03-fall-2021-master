# TODO Do not edit this file directly! Instead, create a new file called
# TODO a03_username.py and copy this code into it!

#################################################################################
# Author: Yin Kyay
# Username: waiy
#
# Assignment: A03 Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1kZhHLMYkN9EUyj44LWp_RjF27UMaWgpc2mObpKcDIuA/edit
#
#################################################################################
# Acknowledgements:

https://www.colorspire.com/rgb-color-wheel/
https://www.webucator.com/article/python-color-constants-module/

#
#
#################################################################################






import turtle


def draw_square(t):


   # the outer square
   r,g,b = 255/255, 215/255, 0/255
   t.fillcolor(r,g,b)
   t.begin_fill()
   for i in range(4):
       t.forward(300)
       t.right(90)
   t.end_fill()


def draw_triangle(t2):
   # triangle
   r,g,b = 255/255,0/255,0/255
   t2.fillcolor(r,g,b)
   t2.begin_fill()
   for i in range(3):
       t2.forward(360)
       t2.left(120)
   t2.end_fill()


def draw_smallwindow(t1):
   r,g,b = 240/255, 238/255, 180/255
   t1.fillcolor(r,g,b)
   t1.begin_fill()
   for i in range(4):
       t1.forward(70)
       t1.right(90)
   t1.end_fill()


def draw_door(t3):
   r, g, b = 255 / 255, 0 / 255, 0 / 255
   t3.fillcolor(r,g,b)
   t3.begin_fill()
   width=100
   height=90
   for i in range(2):
       t3.forward(height)
       t3.right(90)
       t3.forward(width)
       t3.right(90)
   t3.end_fill()


def draw_chimney(t4):
   r, g, b = 148/255, 92/255, 27/255
   t4.fillcolor(r,g,b)
   t4.begin_fill()
   width = 100
   height = 90
   for i in range(2):
       t4.forward(height)
       t4.left(90)
       t4.forward(width)
       t4.left(90)
   t4.end_fill()


def draw_crescent_moon(t5):
   t5.penup()
   t5.left(90)
   t5.forward(200)
   t5.left(90)
   t5.forward(200)
   t5.pendown()
   #fullsize mood
   t5.fillcolor("#F5EBD7")
   t5.begin_fill()
   t5.circle(50)
   t5.end_fill()
   t5.penup()
   t5.forward(20)
   #crescent
   t5.fillcolor('#2C2C2C')
   t5.begin_fill()
   t5.circle(40)
   t5.end_fill()
   t5.pendown()




def main():
       """
       Docstring for main
       """
       # ...
       #Creating the turtle screen
       wn = turtle.Screen()
       wn.bgcolor('#2C2C2C')


       #Creating the turtles
       t=turtle.Turtle()
       t1 = turtle.Turtle()
       t2 = turtle.Turtle()
       t3= turtle.Turtle()
       t4= turtle.Turtle()
       t5= turtle.Turtle()
       t.pensize(10)
       t.speed(10)
       t1.speed(10)
       t1.pensize(10)
       t2.speed(10)
       t2.pensize(10)
       t3.speed(10)
       t3.pensize(10)
       t4.pensize(10)
       t4.speed(5)
       t5.pensize(10)
       t5.speed(5)




#outline of the house
       t.backward(140)
       draw_square(t)
#roof of the house
       t2.backward(170)
       draw_triangle(t2)


# on the way to the window
       t1.penup()
       t1.backward(40)
       t1.right(90)
       t1.forward(40)
       t1.pendown()
#small window on the left
       draw_smallwindow(t1)


# on the way to the window
       t1.penup()
       t1.left(90)
       t1.forward(100)
       t1.pendown()


#small window on the right
       draw_smallwindow(t1)


#on the way to the door
       t3.penup()
       t3.goto(-10,-200)
       t3.backward(30)
       t3.pendown()


#door
       draw_door(t3)


#chimney
       t4.backward(150)
       draw_chimney(t4)


#crescent moon


       draw_crescent_moon(t5)


       wn.exitonclick()


main()

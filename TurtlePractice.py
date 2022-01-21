#house

import turtle

t = turtle.Turtle()


def roof():
    """Draw a triangle to represent a roof"""
    for i in range(3):
        t.lt(120)
        t.forward(100)


def house():
    """Draw a rectangle to represent a house"""
    for i in range(4):
        t.rt(90)
        t.forward(100)


def door():
  #go to starting position
  t.rt(90)
  t.forward(100)
  t.rt(90)
  t.forward(60)

  #draw the door
  t.rt(90)
  t.forward(40)
  t.rt(90)
  t.forward(20)
  t.rt(90)
  t.forward(40)
  t.ht()  # hides the turtle


roof()
house()
door()


turtle.mainloop()

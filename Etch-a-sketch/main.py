from turtle import Turtle, Screen

golu = Turtle()
screen = Screen()

def move_forwards():
    golu.forward(10)

def move_backwards():
    golu.backward(10)

def turn_left():
    golu.left(10)

def turn_right():
    golu.right(10)

def clear():
    golu.clear()
    golu.penup()
    golu.home()
    golu.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "f")
screen.onkey(turn_left, "s")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
clear()


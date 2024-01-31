
from turtle import Turtle,Screen
import random
sc=Screen()
'''
def movf():
    tim.forward(10)
def movb():
    tim.backward(10)

def left():
    new=tim.heading()+10
    tim.setheading(new)
def right():
     new = tim.heading() - 10
     tim.setheading(new)

def clear():
     tim.clear()
     tim.penup()
     tim.home()
     tim.pendown()

sc.listen()
sc.onkey(key="w",fun=movf)
sc.onkey(key="s",fun=movb)
sc.onkey(key="a",fun=left)
sc.onkey(key="d",fun=right)
sc.onkey(key="c",fun=clear)
'''

is_race_on=False
sc.setup(500,400)
user_bet=sc.textinput(title="MAKE YOUR BET",prompt="Which color turtle will win the race?")
colors=["red","orange","yellow","green","blue","purple"]
position=[-70,-40,-10,20,50,80]
all_turtle=[]
for i in range(0,6):
    name=Turtle()
    name=Turtle(shape="turtle")
    name.penup()
    name.color(colors[i])
    name.goto(x=-230,y=position[i])   
    all_turtle.append(name)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on=False

            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"winning color is {winning_color}. you have won the bet")
            else:
                print(f"winning color is {winning_color}. you have lost the bet")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)




sc.exitonclick()

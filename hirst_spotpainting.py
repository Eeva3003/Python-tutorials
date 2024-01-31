# This is a sample Python script.
import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
'''import colorgram
colors=colorgram.extract('ref1.jpeg',10)
rgb_colors=[]

for color in colors:
   r=color.rgb.r
   g=color.rgb.g
   b=color.rgb.b
   new=(r,g,b)
   rgb_colors.append(new)
print(rgb_colors)'''

colors=[(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170)]

no_of_dots=100
tim=Turtle()
tim.speed('fastest')
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
for i in range(1,no_of_dots+1):
   tim.pendown()
   tim.dot(20,random.choice(colors))
   tim.penup()
   tim.forward(50)

   if i % 10 == 0:
      tim.setheading(90)
      tim.forward(50)
      tim.setheading(180)
      tim.forward(500)
      tim.setheading(0)

screen=Screen()
screen.exitonclick()

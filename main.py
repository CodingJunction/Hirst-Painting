import colorgram
import random
from turtle import Turtle,Screen
ob = Turtle()
# Extract 6 colors from an image.
s=Screen()
s.colormode(255)
ob.speed('fastest')
ob.penup()
print(ob.setpos(-240,-240))
ob.pendown()
colors = colorgram.extract('download.jpg',10)
l=[]
for i in colors:
    rgb=i.rgb
    l.append((rgb.r,rgb.g,rgb.b))


for i in range(101):
    if i!=0:
        ob.dot(20,random.choice(l))
    ob.penup()
    ob.forward(50)
    ob.pendown()
    if i%10==0 and i!=0:
        ob.setheading(90)
        ob.penup()
        ob.forward(50)
        ob.pendown()
        ob.setheading(180)
        ob.penup()
        ob.forward(500)
        ob.pendown()
        ob.setheading(0)

        
        
    
s.exitonclick()


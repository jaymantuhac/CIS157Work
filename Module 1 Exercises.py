#Chapter 2 Exercise 5
a = 'All'
b = 'work'
c = 'and'
d = 'no'
e = 'play'
f = 'makes'
g = 'Jack'
h = 'a'
i = 'dull'
j = 'boy.'
print(a, b, c, d, e, f, g, h, i, j)

#Chapter 2 Exercise 7
P = 10000 #Principal amount
n = 12
r = 0.08
t = input("How many years? ")
A = P * (1+ r/n)**(n*int(t))
print(A)

#Chapter 2 Exercise 8
from math import pi

radius = input("What is the radius of your circle? ")
area = pi * (float(radius)**2)
print("Great! The area of your circle is", str(round(area, 2)), "units squared!")

#Chapter 4 Exercise 7
import turtle
wn = turtle.Screen()
wn.bgcolor("white")
drunk_pirate = turtle.Turtle()
drunk_pirate.color("blue")
drunk_pirate.shape("arrow")

experimental_data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

#Initializes drunk_pirate's position forward so path fits the entire screen
drunk_pirate.forward(100)

for angle in experimental_data:
    drunk_pirate.left(angle)
    drunk_pirate.forward(100)

print("The absurdly drunk pirate's final heading is", str(drunk_pirate.heading()))
wn.exitonclick()

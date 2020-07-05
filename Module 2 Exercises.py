#Chapter 5 Exercise 18
import math

def hypotenuse(x, y): #each variable represents length of 1 side of the right triangle
    return math.hypot(x,y)

print(hypotenuse(1, 3))

#Chapter 5 Exercise 19
"""
The following approximation method uses the perimeter of a polygon in order
to estimate the value of pi. Asuming that the distance from the center
of the polygon to the nearest side is kept constant at 1 unit,
as you increase the number of sides of the regular polygon, the perimeter of that
polygon will reach closer to the value of pi.

Approximation method is found through this link,
including the formulas used in the approximation:
https://www.desmos.com/calculator/p3zeajcgle
"""

from math import tan, pi

def polygon_perimeter(n):
    one_side = (tan((pi/n) - pi) - tan(-(pi/n)))
    return (n * one_side)/2

print("The approximate value of pi is:",polygon_perimeter(30))
print("The actual value of pi is:",pi)


#Chapter 6 Exercise 3
import turtle

def drawPoly(someturtle, somesides, somesize):

    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

wn = turtle.Screen()
wn.bgcolor("white")
jay = turtle.Turtle()

drawPoly(jay, 20, 30)

#Chapter 6 Exercise 14
import math

def mySqrt(n):
    """
    Note: Exercise instructions do not define how many guesses should be made.
    I added the functionality of asking for the number of guesses in order
    to use iteration to execute this function
    """
    number_of_guesses = int(input("How many guesses would you like to make: "))
    initial_guess = n/2
    current_guess = initial_guess
    for i in range(number_of_guesses):
        new_guess = (1/2) * (current_guess + (n/current_guess))
        current_guess = new_guess
    return current_guess

print(mySqrt(2)) #I used an input of 4 in this test
print("The actual value is", math.sqrt(2))

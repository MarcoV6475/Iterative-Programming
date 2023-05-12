#Marco Villegas
#5/12/23

#Problem 1
print("\n\nProgram 1")
n=100
for i in range(0, n):
    print(i, "Hello World")
#This program will print the phrase "Hello World" 100 times




#Problem 2
print("\n\nProgram 2")
n = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for item in n:
    print(item)

for item in n:
    print("The square of",item,"is", item**2)
#This program will print out the numbers seen below and then
#it will print out the the square of each number in a new line



    
#Problem 3
print("\n\nProgram 3")
import turtle

polygon_sides = [int(input("Please enter the number of sides of the polygon "
                           "you want the turtle to draw: (as a number) "))]
length_side = int(input("Enter the length of the side: (as a number) "))
color_side = input("Which color do you want the pen to be? ")
fill_polygon = input("With which color do you want to fill the polygon? ")

wn = turtle.Screen()
wn.bgcolor("lightblue")
marco = turtle.Turtle()
marco.shape("circle")

marco.begin_fill()

for i in range(polygon_sides[0]):
    marco.color(color_side, fill_polygon)
    marco.forward(length_side)
    marco.left(180 - (180 * (polygon_sides[0] - 2)) // polygon_sides[0])

marco.end_fill()
#This program asks the user for the number of sides, the length of the side
#the color of the line and to fill the color of the program. Finally the
#circle will draw the polygon. 







#Problem 4
print("\n\nProgram 4")
n=50
while(n<0):
    n = int(input("Enter the ending integer: "))
    
for n in range(1, n+1):

    if n%3 == 0 and n%5 == 0:
        print("Divisble by both!",end=" ")
    elif n % 3 == 0:
        print("Divisible by 3!", end = " ")
    elif n % 5 == 0:
        print("Divisible by 5!", end = " ")
    else:
        print(n, end = " ")
#This program iterates the integers from 1-50; it then ask for the
#programmer to see if it is divisible by 3 or not; which will print out a
#statement saying if it is divisible or not. Next, it will ask
#if those same numbers, 1-50, are divisible by by 5 or not; once again asking
#the program to say in writing if it is divisible by 5 or not. Finally, the
#last code will ask to see if the numbers from, 1-50, are divisible by both,
#3 and 5, or not.





        
#Problem 5
print("\n\nProgram 5")
print("Your star will now be created!")
import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

marco = turtle.Turtle()
marco.left(36)
marco.color("yellow")
marco.pensize(5)

for i in range(5):
    marco.forward(150)
    marco.left(144)

wn.exitonclick()
#This program will have a light blue background and it will create a star!
#The program will import turtle and then start creating the shape of a star.



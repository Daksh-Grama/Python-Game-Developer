import turtle
screen = turtle.Screen()

clr = input("Pick a color : R/G/B - ")

if clr == "R" :
    turtle.color("red")

elif clr == "G" :
    turtle.color("green")

elif clr == "B" :
    turtle.color("blue")

else :
    print("Invalid selection")

sides = int(input("How many sides does your shape have (3-10) : "))   
for i in range (sides):
    turtle.forward(100)
    turtle.left(360/sides) 

screen.mainloop()         
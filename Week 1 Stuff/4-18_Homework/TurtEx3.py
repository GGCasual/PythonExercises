from turtle import *
import random
window = Screen()
sides = Turtle()

#7. Circle
# from turtle import *
pencolor('green')

circle(180)
pencolor('cyan')
#2. Square
# from turtle import *

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

# mainloop()

#1. Equilateral Triangle

for i in range(3):
    sides.forward(300)
    sides.left(360/3)

# window.exitonclick()

#3. Pentagon
# from turtle import *

# window = Screen()
# sides = Turtle()

for i in range(5):
    sides.forward(100)
    sides.left(360/5)
pencolor('red')
# window.exitonclick()

#4. Hexagon
# from turtle import *

# window = Screen()
# sides = Turtle()

for i in range(6):
    sides.forward(100)
    sides.left(360/6)

# window.exitonclick()

#5. Octagon
# from turtle import *

# window = Screen()
# sides = Turtle()

for i in range(8):
    sides.forward(75)
    sides.left(360/8)

# window.exitonclick()

#6. Star
# from turtle import *

for i in range(5):
    forward(100)
    right(144)

mainloop()






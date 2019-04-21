from turtle import *

window = Screen()
sides = Turtle()
bgcolor('black')
pencolor('yellow')

for i in range(5):
    forward(100)
    right(144)

for i in range(5):
    backward(100)
    left(144)

for i in range(5):
    forward(200)
    right(144)

for i in range(5):
    backward(200)
    left(144)

for i in range(5):
    right(144)
    backward(100)

for i in range(5):
    left(144)
    forward(100)

for i in range(5):
    right(144)
    backward(200)

for i in range(5):
    left(144)
    forward(200)

mainloop()
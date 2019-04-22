# 1. Hello
# name1 = input("What's your name? ")

# def hello(name1):
#     print("Hello, " + name1)

# hello(name1)

# 2. y = x + 1
# import matplotlib
# from matplotlib import pyplot as plot

# def f(x):
#     return x + 1

# xs = list(range(-3, 4))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# 3. Square of x
# import matplotlib
# from matplotlib import pyplot as plot

# def f(x):
#     return x * x

# xs = list(range(-100, 100))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# 4. Odd or Even
# import matplotlib
# from matplotlib import pyplot as plot

# def f(x):
#     if x % 2 != 0:
#         return 1
#     if x % 2 == 0:
#         return -1

# xs = list(range(-5, 5))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.bar(xs, ys)
# plot.show()

# 5. Sine
# import math
# import matplotlib
# from matplotlib import pyplot as plot

# def f(x):
#     return math.sin(x)

# xs = list(range(-5, 6))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# 6. Sine 2
# import math
# import matplotlib
# from matplotlib import pyplot as plot
# from numpy import arange

# def f(x):
#     return math.sin(x)

# xs = list(arange(-5, 6, 0.1))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# 7. Degree Conversion
# import matplotlib
# from matplotlib import pyplot as plot

# cels = int(input("Type a temperature in Celsius? "))

# def farenh(cels):
#     return x * 1.8 + 32

# xs = list(range(-10, 100))
# ys = []

# for x in xs:
#     ys.append(farenh(x))

# plot.plot(xs, ys)
# plot.show()

# 8. Play again?
question = input("Do you want to play again (Y or N)? ")


def answer():
    if answer == "Y": 
        print("True")
    if answer == "N":
        print("False")

answer(question)

# 9. Play again? Again.


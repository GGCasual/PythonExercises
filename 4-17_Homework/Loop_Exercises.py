# 1. 1 to 10
# for number in range(1,11):
#     print(number)

# 2. n to m
# num1 = int(input("Start from: "))
# num2 = int(input("End on: ")) + 1

# for number in range(num1,num2):
#     print(number)

# 3. Odd Numbers
# for number in range(0,11):
#     if number % 2 != 0:
#         print(number)

# 4. Print a Square
# for i in range(5):
#     print("*****")

# 5. Print a Square II
# num = int(input("How big would you like your square to be? "))

# for i in range(num):
#     print('*' * num)

# 6. Print a Box
# height = int(input("Specify the height: "))
# width = int(input("Specify the width: "))

# for w in range(width):
#     for h in range(height):
#         print('* ' if w in [0, height-1] or h in [0, width-1] else '  ', end='')
#     print()

# 7. Print a Triangle
# num = 4
# row = 0

# while row < num:
#     space = num - row - 1
#     while space > 0:
#         print(end = " ")
#         space = space - 1
#     star = row + 1
#     while star > 0:
#         print("*", end = " ")
#         star = star - 1
#     row += 1
#     print()

# 8. Print a Triangle II
# num = int(input("Enter a number: "))
# row = 0

# while row < num:
#     space = num - row - 1
#     while space > 0:
#         print(end = " ")
#         space = space - 1
#     star = row + 1
#     while star > 0:
#         print("*", end = " ")
#         star = star - 1
#     row += 1
#     print()

# 9. Multiplication Table
# for outer in range(1, 11):
#     for inner in range(1, 11):
#         result = outer * inner
#         print(f"{outer} x {inner} = {result}")
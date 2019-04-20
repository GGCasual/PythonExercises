num = int(input("I\'m thinking of a number between 1 and 10. What is it? You can only guess 5 times. "))
import random
random_secret_num = random.randint(1, 10)
guesses = 5

while num != random_secret_num:
    guesses -= 1
    if guesses == 0:
        print("Sorry, you lost!")
        break
    if num < random_secret_num:
        print("Nope, try again!")
        print(str(num) + " is too low. You have " + str(guesses) + " left.")
    elif num > random_secret_num:
        print("Nope, try again!")
        print(str(num) + " is too high. You have " + str(guesses) + " left.")
    num = int(input("Guess another number: "))

if random_secret_num == num:
    print("Congrats! You got it right!") 
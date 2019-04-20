# 1. Hello, you!
# name = input("What\'s your name?")
# print('Hello, ' + name + "!")

# 2. HELLO, YOU! 
# name = input("WHAT\'S YOUR NAME? ")
# print('HELLO, ' + name.upper() + "!")

# number = len(name)
# print ('YOUR NAME HAS ' + str(number) + ' LETTERS IN IT! AWESOME!')

# 3. Madlib
# name = input("Enter your name: ")
# subj = input("What\'s your favorite subject? ")

# print(name + "\'s favorite subject in school is " + subj + ".")
# print("What\'s the name? " + name)
# print("What\'s the subject? " + subj)

# 4. Day of the Week
# day = int(input('Day (0-6)? '))

# if(day == 0):
#     print("Sunday")
# elif(day == 1):
#     print("Monday")
# elif(day == 2):
#     print("Tuesday")
# elif(day == 3):
#     print("Wednesday")
# elif(day == 4):
#     print("Thursday")
# elif(day == 5):
#     print("Friday")
# elif(day == 6):
#     print("Saturday")
# else:
#     print("Invalid number.")

# 5. Work or Sleep In?
# day = int(input('Day (0-6)? '))

# if(day == 0 or day == 6):
#     print("Sleep in.")
# elif(day > 0 and day <= 5):
#     print("Go to work!")
# else:
#     print("Invalid number.")

# 6. Celsius to Farenheit
# cel_temp = float(input("Temperature in C? "))
# fare_temp = cel_temp * 1.8 + 32

# print(str(fare_temp) + " F")

# 7. Tip Calculator 
# bill_amount = float(input("Total bill amount? "))
# service_quality = input("Level of service? ")
# tip_amount = float() 
# total = float() 

# if service_quality == 'good':
#     tip_amount = bill_amount * .20
#     print("Tip amount: ${:.2f}".format(tip_amount))
#     total = tip_amount + bill_amount
#     print("Total amount: ${:.2f}".format(total))
# elif service_quality == 'fair':
#     tip_amount = bill_amount * .15
#     print("Tip amount: ${:.2f}".format(tip_amount))
#     total = tip_amount + bill_amount
#     print("Total amount: ${:.2f}".format(total))
# elif service_quality == 'bad':
#     tip_amount = bill_amount * .10
#     print("Tip amount: ${:.2f}".format(tip_amount))
#     total = tip_amount + bill_amount
#     print("Total amount: ${:.2f}".format(total))

# 8. Tip Calculator 2
# bill_amount = float(input("Total bill amount? "))
# service_quality = input("Level of service? ")
# num_people = int(input("Split how many ways? "))
# tip_amount = float() 
# total = float()
# person_cost = float()

# if service_quality == 'good':
#     tip_amount = bill_amount * .20
#     print("Tip amount: ${:.2f}".format(tip_amount))
#     total = tip_amount + bill_amount
#     print("Total amount: ${:.2f}".format(total))
#     person_cost = total / num_people
#     print("Amount per person: ${:.2f}".format(person_cost))
# elif service_quality == 'fair':
#     tip_amount = bill_amount * .15
#     print("Tip amount: ${:.2f}".format(tip_amount))
#     total = tip_amount + bill_amount
#     print("Total amount: ${:.2f}".format(total))
#     person_cost = total / num_people
#     print("Amount per person: ${:.2f}".format(person_cost))
# elif service_quality == 'bad':
#     tip_amount = bill_amount * .10
#     print("Tip amount: ${:.2f}".format(tip_amount))
#     total = tip_amount + bill_amount
#     print("Total amount: ${:.2f}".format(total))
#     person_cost = total / num_people
#     print("Amount per person: ${:.2f}".format(person_cost))

# 9. 1 to 10
# num = 0
# while(num < 10):
#     num += 1
#     print(num)

# 10. How many coins? 
# coins = 0
# answer = input("You have " + str(coins) + " coin(s). Do you want another? ")

# while answer != 'no':
#     coins += 1 
#     print("You now have " + str(coins) + " coin(s).")
#     answer = input("Do you want another? ")
# print("Bye!")

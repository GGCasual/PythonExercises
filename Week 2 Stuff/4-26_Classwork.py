# class Character(object):
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
#     def printMyself(self):
#         print("I am a hero.")
#     def attack(self):
#         pass

# class Hero(Character):
#     def __init__(self, health, power):
#         super(Hero, self).__init__(health, power) ## super(works here too)


# class Goblin(Character):
#     pass



# hero = Hero(5, 10)
# goblin = Goblin(4, 8)


# print(hero.health)
# hero.printMyself()
# goblin.printMyself()







# file_handler = open('file.txt', 'r')

# contents = file_handler.read()

# file_handler.close()

# print(contents)

file_handler = open('file.txt', 'w')
file_handler.write("Thank God it\'s Friday")
file_handler.close()


## For Friday's Homework
python3 -m pip install --user numpy

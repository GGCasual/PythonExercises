class Character(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def printMyself(self):
        print("I am a hero.")
    def attack(self):
        pass

class Hero(Character):
    def __init__(self, health, power):
        super(Hero, self).__init__(health, power) ## super(works here too)


class Goblin(Character):
    pass



hero = Hero(5, 10)
goblin = Goblin(4, 8)


print(hero.health)
hero.printMyself()
goblin.printMyself()
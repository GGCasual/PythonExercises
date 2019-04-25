# # 1. Basics
class Person(object):
    def __init__(self, name, email, phone, friends): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0
    def greet(self, other_person): 
        print(f"Hello {other_person.name}, I am {self.name}!")
    def print_contact_info(self):
        print(f"{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}")
    def add_friend(self, other_person):
        self.friends.append(other_person)
    def number_friends(self):
        print(f"I have {len(self.friends)} friend(s)")
    def print_friends(self):
        for personObject in self.friends:
            print(f"{personObject.name} {personObject.email} {personObject.phone}")


### __str__
def __str__(self): 
    return 'Person: {} {} {}'.format(self.name, self.email, self.phone)



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


print(jordan)


# sonny.greet(jordan)
# jordan.greet(sonny)

# print(f"Sonny\'s info: {sonny.email}, {sonny.phone}")
# print(f"Jordan\'s info: {jordan.email}, {jordan.phone}")


# # Add a method 2
# sonny.print_contact_info()
# jordan.print_contact_info()


# # Add a add_friend method
jordan.add_friend(sonny)
sonny.add_friend(jordan)

# # Add a num_friends method
jordan.number_friends()

# # Count number of greetings
print(jordan.greeting_count)



# #2. Make you own class
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def printInfo(self):
        print(f"{self.year} {self.make} {self.model}")


car = Vehicle('Nissan', 'Leaf', 2015)

print(car.make, car.model, car.year)





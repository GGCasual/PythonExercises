# # 1. Basics
class Person(object):
    def __init__(self, name, email, phone, friends): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = friends
    def greet(self, other_person): 
        print(f"Hello {other_person.name}, I am {self.name}!")
    def print_contact_info(self):
        print(f"{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}")




sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


# sonny.greet(jordan)
# jordan.greet(sonny)

# print(f"Sonny\'s info: {sonny.email}, {sonny.phone}")
# print(f"Jordan\'s info: {jordan.email}, {jordan.phone}")


# # Add a method 2
# sonny.print_contact_info()

# # Add an instance variable(attribute)
friends.append(sonny) 
friends.append(jordan)

print(f"{self.friends}")

# # Add a add_friend method

# # Add a num_friends method

# # Count number of greetings




# # 2. Make you own class
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def printInfo(self):
#         print(f"{self.year} {self.make} {self.model}")


# nissan = Vehicle('Nissan', 'Leaf', '2015')

# # # Add a method
# nissan.printInfo()
# # 1. Basics
class Person:
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 

    def greet(self, other_person): 
        print(f"Hello {other_person.name}, I am {self.name}!")

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)
print(f"Sonny\'s info: {sonny.email}, {sonny.phone}")


# # 2. Make you own class

# # Add a method

# # Add a method 2

# # Add an instance variable(attribute)

# # Add a add_friend method

# # Add a num_friends method

# # Count number of greetings
# student1 = 'Tarek'
# student2 = 'Chris'
# student3 = 'Michael'

# def Students():
#     print(f"{student1} {student2} {student3}")

# Students()

# student1 = "Glenn"

# Students()

# class Students:
#     def PrintStudents():
#         print("Tarek Chris Michael")



# class Students:

#     def students(self):
#         print("Tarek Chris Michael")

# Michael = Students()
# Michael.students()

# Chris = Students()
# Chris.students()



# class MyClass(object):
#     def __init__(self, first_name, last_name):
#         print("hello world")
#         self.first_name = first_name
#         self.last_name = last_name
#     def printName(self):
#         # name = "Celeste"
#         print(f"{self.first_name} {self.last_name}")

# dc = MyClass('Chris', 'Humphrey')
# dc.printName()

# dc_houston = MyClass('Mohammad', 'Azam')
# dc_houston.printName()




class Person(object):
    def __init__(self, name):
        self.name = name
        self.count = 0
        print(f"hello {self.name}")
    def change_name(self, new_name):
        self.name = new_name
        self.count = self.count + 1
        print(f"name: {self.name} count: {self.count}")


student = Person('veronica')
# #atlanta_student = Person("Michael", "atalanta_student")
student.change_name("Matt")
student.change_name("Matt1")
student.change_name("Matt2")
student.change_name("Matt3")
# #atlanta_student.change_name("Jake")

student.change_name("Matt4")
student.change_name("Matt5")
student.change_name("Matt6")
student.change_name("Matt7")
# #atlanta_student.change_name("Jake1")




# class Phone(object):
#     def __init__(self, phone_type):
#         self.phone_type = phone_type
#         self.status = 'off'
#     def print_phone(self):
#         print(self.phone_type)
#     def on(self):
#         print('on')
#         self.status = 'on'
#     def off(self):
#         print('off')
#         self.status = 'off'
#     def get_status(self):
#         print(f'your {self.phone_type} phone is currently: {self.status}')


# android = Phone('android')
# iPhone = Phone('iPhone')
# blackberry =Phone('blackberry')

# android.get_status()
# android.on()
# android.get_status()

# iPhone.get_status()

# blackberry.get_status()




# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.doorStatus = "closed"
#         print(f"make: {self.make} model: {self.model} color: {self.color}")
#     def ChangeColor(self, newColor):
#         self.color = newColor
#         return (self.color)
#     def openDoor(self):
#         self.doorStatus = "open"
#     def displayColor(self):
#         print(f"The color of your {self.make} is {self.color}")
#     def displayInfo(self):
#         print(f"make: {self.make} model: {self.model} color: {self.color}")



# toyota = Car("toyota", "prius", "green")
# honda = Car("honda", "civic", "purple")
# jeep = Car("jeep", "wrangler", "white")
# ford = Car("ford", "f150", "marble")

# ford.ChangeColor("midnight red")
# ford.displayColor()

# toyota.displayInfo()
# honda.displayInfo()

# fleet = [toyota, honda, jeep, ford]

# for carObject in fleet:
#     print(carObject.displayInfo())
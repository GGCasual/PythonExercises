

class Student(object):
    def __init__(self, firstName, lastName, campus):
        self.firstName = firstName
        self.lastName = lastName
        self.campus = campus
    def printStudent(self):
        print(f"{self.firstName} {self.lastName} campus: {self.campus}")

# ## One Way of Printing
# Sabrina = Student("Sabrina", "Goldfarb", "Houston")
# Alfie = Student("Alfie", "Santos", "Houston")
# Michael = Student("Michael", "Dao", "Houston")
# Cindy = Student("Cindy", "Smith", "Atlanta")

class Campus(object):
    def __init__(self):
        self.students = []
    def addStudent(self, firstName, lastName, campus):
        temp = Student(firstName, lastName, campus)
        self.students.append(temp)
    def showCurrentStudents(self):
        for studentObject in self.students:
            print(f"{studentObject.firstName} {studentObject.lastName}")

## Second Way of Printing
management = Campus()

management.addStudent("Sabrina", "Goldfarb", "Houston")
management.addStudent("Alfie", "Santos", "Houston")
management.addStudent("Michael", "Dao", "Houston")
management.addStudent("Cindy", "Smith", "Atlanta")

management.showCurrentStudents()






# class Member():
#     def __init__(self, firstName, lastName, account_num, credit_score):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.account_num = account_num
#         self.credit_score = credit_score
#     def showMemberInfo(self):
#         print(f"{self.firstName} {self.lastName} Account Number: {self.account_num}, Credit Score: {self.credit_score}")


# class Bank(object):
#     def __init__(self):
#         self.members = []
#     def addMember(self, firstName, lastName, account_num, credit_score):
#         temp = Member(firstName, lastName, account_num, credit_score)
#         self.members.append(temp)
#     def showCurrentMembers(self, firstName, lastName, account_num, credit_score):
#         for mem in self.members:
#             print(f"{self.firstName} {self.lastName} {account_num} {credit_score}")


# management = Bank()

# Ben = ("Ben", "Jones", "1422434112", "823")
# Lacy = ("Lacy", "Jones", "35452342234", "810")

# management.showCurrentMembers()
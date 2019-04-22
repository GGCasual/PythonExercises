# DICTIONARIES

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }

# isItThere = "wat" in my_dictionary
# print(isItThere)

# my_dictionary["theMeaningOfLife"] = "wat"
# wat = my_dictionary["theMeaningOfLife"]
# print(wat)

# my_dictionary["newKeyName"] = "hello world"
# print(my_dictionary)

# keys = my_dictionary.keys()
# print(keys)

# values = my_dictionary.values()
# print(values)

# del my_dictionary["theMeaningOfLife"]
# print(my_dictionary)

# items = my_dictionary.items()
# print(items)

# for key, value in my_dictionary.items():
#     print(key)
#     print(value)





# whoa = {
#     "mindIsBlown" : {
#         "theMeaningOfLife" : 42
#     },
#     "toDoList" : ["sing", "laugh", "dance", "cry"]
# }

# helloIs = my_dictionary["hello"]
# print(helloIs)

# watIs = my_dictionary.get["wat"]
# print(watIs)





# contact = [
#     {
#         'first_name': 'Phillip',
#         'last_name': 'Guo',
#         'email': 'phillip.guo@gmail.com',
#         'phone':{
#             'work':'837-494-3948',
#             'cell': '234-897-4933'
#         }
#     },
#     {
#         'first_name': 'Mark',
#         'last_name': 'Guzdial',
#         'email': 'mark.guzdial@gatech.edu',
#         'phone':{
#             'work':'484-569-3466',
#             'cell': '493-485-9845'
#         }
#     }
# ]















# # ERRORS AND DEBUGGING
# while True:
#   try:
#     x = int(input("Please enter a number: "))
#     break
#   except ValueError:
#     print("Oops!  That was no valid number.  Try again...")

#     try:
#   do_something()
# except Error1:
#   failure1()
# except Error2:
#   failure2()
# else:
#   only_execute_when_successful()
# finally:
#   always_execute()

#   raise NameError('Hi There')
# raise ValueError
# class MyError(Exception):
#   pass

#   # mymodule.py
# def test ():
#   name = "Narf"
#   print(name[10])
#   print("done")
# if __name__ == '__main__':
#   test()
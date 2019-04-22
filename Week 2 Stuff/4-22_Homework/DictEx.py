# # 1. Exercise 1
# phonebook_dict = { 
#     'Alice': '703-493-1834', 
#     'Bob': '857-384-1234', 
#     'Elizabeth': '484-584-2923'
# }

# Eli = phonebook_dict.get("Elizabeth")
# print(Eli)

# Kareem = {'Kareem': '938-489-1234'}
# phonebook_dict['Kareem'] = '938-489-1234'
# print(Kareem)
# print(phonebook_dict)

# del phonebook_dict['Alice']
# print(phonebook_dict)

# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)



# # 2. Exercise 2: Nested Dictionaries
# ramit = { 
#     'name': 'Ramit', 
#     'email': 'ramit@gmail.com', 
#     'interests': ['movies', 'tennis'], 
#     'friends': [ 
#     { 
#         'name': 'Jasmine', 
#         'email': 'jasmine@yahoo.com', 
#         'interests': ['photography', 'tennis']
#     }, 
#     { 
#         'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] 
#     } 
#     ] 
# }

# print(ramit['email'])

# print(ramit['interests'][0])

# print(ramit['friends'][0]['email'])

# print(ramit['friends'][1]['interests'][1])



# # 3. Letter Summary
# word = "banana"

# letters = {
#     'a':'','b':'','n':'' 
# }

# letters['a'] = word.count('a')
# letters['b'] = word.count('b')
# letters['n'] = word.count('n')

# print(f"Letter Histogram: {word}")
# print(letters)



# # 4. Word Summary
# word = "to be or not to be"

# words = {
#     'to':'','be':'','or':'','not':''
# }

# words['to'] = word.count('to')
# words['be'] = word.count('be')
# words['or'] = word.count('or')
# words['not'] = word.count('not')

# print(f"Word Histogram: {word}")
# print(words)
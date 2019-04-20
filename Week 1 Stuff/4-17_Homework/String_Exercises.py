# 1. Uppercase a String
# string1 = input("Enter word(s): ")
# print(string1.upper())

# 2. Capitalize a String
# string1 = input("Enter word(s): ")
# print(string1.capitalize())

# 3. Reverse a String
# string1 = input("Enter word(s): ")
# print(string1[::-1])

# 4. Leetspeak
# word = input("Type word(s): ").lower()

# for char in word:
#     if char == 'a':
#         word = word.replace('a','4')
#     elif char == 'e':
#         word = word.replace('e','3')
#     elif char == 'g':
#         word = word.replace('g','6')
#     elif char == 'i':
#         word = word.replace('i','1')
#     elif char == 'o':
#         word = word.replace('o','0')
#     elif char == 's':
#         word = word.replace('s','5')
#     elif char == 't':
#         word = word.replace('t','7')
# print(word)

# 5. Long-long Vowels
# word = input("Type a word: ")

# word = word.replace('aa', 'aaaaa')
# word = word.replace('ee', 'eeeee')
# word = word.replace('ii', 'iiiii')
# word = word.replace('oo', 'ooooo')
# word = word.replace('uu', 'uuuuu')

# print(word)

# 6. Caesar Cipher
# secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
# offset = 13
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# result = ''

# for char in secret:
#     ascii_code = ord(char)
#     is_uppercase = ascii_code >= 65 and ascii_code <= 90
#     char = char.lower()
#     if char not in alphabet:
#         new_char = char
#     else:
#         idx = alphabet.find(char)
#         new_idx = idx + offset
#         if new_idx > 25:
#             new_idx = new_idx - 26
#         new_char = alphabet[new_idx]
#         if is_uppercase:
#             new_char = new_char.upper()
#     result += new_char

# print(result)
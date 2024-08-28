# === 3.1 ===

# x = 1
# while x <= 42:
#     print(f'I love python {x}')
#     x += 1

# === 3.2 ===

# age_in_month = 2000
# age_in_years = 40
# my_name = 'Maksym'
# my_age = "My name is " + my_name + ", " + "I am " + str(age_in_years) + " old."
# print(my_age)

# === 3.3 ===

# i = 1
# print(i == 1)
# print(i == '1')
# print(i == '')
# print(i == 2)
# print(i != 0)

# === 3.4 ===

# a = 2
# b = 5
# c = 6
# d = str(a) + str(b) + str(c)
# print(d)

# === 4.1 ===

# user_input = input('Enter some text: ')
# if user_input.isnumeric():
#     print(f'Entered value `{user_input}` is a number')
# else:
#     print(f'Entered value `{user_input}` is a text')

# === 4.2 ===

# digits = input('Enter a digit: ')
# if digits.isnumeric():
#     digits = int(digits)
#     if digits > 0 and digits % 2 == 0:
#         print(f'The number `{digits}` is even')
#     else:
#         print(f'The number `{digits}` is odd')
# else:
#     print(f'The value `{digits}` is not a number')

# === 4.3 ===

# text = input('Enter any text: ')
# n = len(text)
# print(f'The length of `{text}` is - {n}')

# === 4.4 ===

# text = input('Enter a text: ')
# n = len(text)
# if text.isnumeric():
#     text = int(text)
#     if text > 0 and text % 2 == 0:
#         print(f'Entered value `{text}` is an even number')
#     else:
#         print(f'Entered value `{text}` is an odd number')
# else:
#     print(f'Entered value `{text}` is a text with length {n}')

# === 5.1 ===

# info = input('Enter your value: ')
# for i in info:
#     if i.isnumeric():
#         i = int(i)
#         if i % 2 == 0:
#             print(f'The symbol `{i}` is an even digit')
#         else:
#             print(f'The symbol `{i}` is an odd digit')
#     elif i.isupper():
#         print(f'The symbol `{i}` is an uppercase letter')
#     elif i.islower():
#         print(f'The symbol `{i}` is an lowercase letter')
#     else:
#         print(f'The symbol `{i}` is neither a digit nor a letter')

# === 5.2 ===

# while True:
#     command = input('Enter your command: ')
#     if command == 'exit':
#         break
#     else:
#         print(command)

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

# === 5.3 ===

# while True:
#     command = input('Enter your command: ')
#     command = command.strip().lower()
#     if command == 'exit':
#         break
#     else:
#         print(command)

# === 6.1 ===

# def say_func():
#     print('I am a Function')
# say_func()

# === 6.2 ===

# def check_age(age):
#     if age <= 0 or age > 110:
#         print('Error')
#     elif age >= 18:
#         print("Adult")
#     else:
#         print('Child')
# check_age(-4)
# check_age(0)
# check_age(17)
# check_age(18)
# check_age(21)
# check_age(110)
# check_age(111)

# === 6.3 ===

# def power_two(n):
#     return pow(n, 2)
# print(power_two(4))

# === 6.4 ===

# def text_len(text):
#     return len(text)
# res = text_len('some text!')
# print(res)

# === 6.5 ===

# def power_two(n):
#     return pow(n, 7)
# print(power_two(2))

# === 6.6 ===

# def split_text(text):
#     return text.split()
# print(split_text('mY new text'))

# === 6.7 ===

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     else:
#         return True 
# print(is_prime(7))

# === 7.1 ===

# def args_len(*args):
#     return len(args)
# res = args_len(1, 2, 3, 'sdd', True)
# print(res)

# === 7.2 ===

# def has_42(*args):
#     if 42 in args:
#         return True
#     else:
#         return False
# res = has_42('42', 32, 33, 3, 3, 2)
# print(res)
    
# === 7.3 ===

# def check_even():
#     return print(list(filter(lambda x: x % 2 == 0, [1, 21, 22, 32, 33, 12])))
# check_even()

# === 7.4 ===

# nums = [32, -12, 3, -7, -9]
# def mirror(x):
#     return print(list(map(lambda x: x * -1, x)))
# mirror(nums)

# === 7.5 ===

# def make_adder(n):
#     def added(x):
#         return n + x
#     return added
# adder = make_adder(5)
# print(adder(10))

# === 9.1 ===

# def is_in_list(lst, value):
#     if value in lst:
#         return True
#     else:
#         return False
# print(is_in_list([1, 2, 3, 4, 42], 5))

# === 9.2 ===

# def add_to_list(lst, value):
#     lst.append(value)
#     return lst
# print(add_to_list([1, 2, 3, 4, 5], 9))

# === 9.3 ===

# def add_to_list_index(lst, value, index = None):
#     if index == None:
#         lst.append(value)
#         return lst
#     else:
#         lst.insert(value, index)
#         return lst
# print(add_to_list_index([1, 2, 3, 4, 5], 0))
# print(add_to_list_index([1, 2, 3, 4, 5], 3, 0))

# === 9.4 ===

# def remove_from_list(lst, index):
#     del lst[index]
#     return lst
# print(remove_from_list([1, 2, 3, 4, 5, 6, 7], -1))

# === 9.5 ===

# def slice(lst, start, end):
#     new_lst = lst[start:end]
#     if start < end and end < len(lst):
#         print(True)
#         print(len(lst))
#     else:
#         print(False)
#     return new_lst
# print(slice([1, 2, 3, 4, 5], 1, 4))

# === 9.6 ===

# def unique(lst):
#     new_list = []
#     for i in lst:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# print(unique([1, 2, 3, 2, 1, 1, 3, 5, 6, 7, 34, 34, 34, 4]))

# === 9.7 ===

# def merge(tuple1, tuple2):
#     return tuple1 + tuple2
# print(merge((1, 2, 3), (4, 5, 6)))

# === 10.1 ===
test_dict = {'max': 12345, 'Olek': 67890}

# def init():
#     phones = dict()
#     return phones
# init()

# def add_to_dict():
#     res = dict()
#     name_key = input('Enter the Name: ')
#     number_value = input('Enter a phone number: ')
#     res[name_key] = number_value
#     print(res)
# add_to_dict()

def remove_from_dict(dict, key):
    if key in dict:
        del dict[key]
    else:
        return
print(remove_from_dict(test_dict, 'Olek'))

# def value_by_key(dict, key):
#     if key in dict:
#         return dict[key]
#     else:
#         return None
# print(value_by_key(test_dict, 'qwe'))

# def list_of_keys(dict):
#     return dict.keys()
# print(list_of_keys(test_dict))

# def key_exist(dict, key):
#     if key in dict:
#         return True
#     else:
#         return False
# print(key_exist(test_dict, 'rio'))
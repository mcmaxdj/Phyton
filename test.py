# i = 1
# test = 'This is a test'
# foo = "bar"

# my_age = 40
# my_age += 1
# my_name = "Maksym"

# my_data = my_name + str(my_age)

# print(my_data)
# ========================

# class MyTest:
#     x = 1

# def my_func():
#     return 1

# x = 12
# if x >= 0:
#     print('positive number')
# elif x <= 0:
#     print('negative number')
# else:
#     print('what is it?')

# y = 11
# if y == 0:
#     print('zero')
# elif y > 0:
#     if y % 2:
#         print('this number is odd')
#     else:
#         print('this number is even')
# else:
#     print('Negative')

# y = 21
# if y == 0:
#     print('zero')
# elif y > 0 and y % 2 == 0:
#     print('this number is even')
# elif y > 0 and y % 2 == 1:
#     print('this number is odd')
# else:
#     print('Negative')

# y = 21
# if y == 0:
#     print('zero')
# elif y > 0 or y == -42:
#     print('test condition')
# else:
#     print('Negative')

# a = 1
# b = 0

# if a < 0:
#     print('a < 0')
# elif b == 0:
#     print('b == 0')

# =========== Out of the box functions ===========

# int() - convert data to integer type
# list() - convert data to the list or create new ampty list
# range() - creating a sequence of numbers
# set() - convert data to the SET or create new ampty SET
# str() - convert data to the string
# tuple() - convert data to the tuple or create new ampty tuple
# input() - user input via stdin
# print() - output data to the terminal (stdout)
# len() - to know the length of objects
# sorted() - return sorted list
# type() - defining an object type or creating a new one
# help() - show info about function or objects

# .isalpha() - return True if value is aplphabetic
# .isupper() - return True if all parts of the text is uppercase
# .islower() - return True if all parts of the text is lowercase
# .istitle() - return True if every word starts from uppercase
# .isnumeric() - return True if value is digit
# .isdigit() - return True if all parts of the text is digits

# x = 'some text'
# print(x.isupper())

# .upper() - convert text to uppercase
# .lower() - convert text to lowercase
# .split(s) - splits the text according to the passed delimiter. if it is not passed, it divides the text with a space.
# .title() - conver every first letter in the text to uppercase
# .capitalize() - convert first letter to uppercase
# .count(c) - returns the number of characters passed in the text

# text = 'some Text'
# print(text.split('e'))

# =====================

# x = 'This'
# y = 'is'
# z = 'test'
# print(x + " " + y + " " + z)
# print(f'{x} {y} {z}') # f-string 

# ===================== INPUT/OUTPUT

# print('Start...')
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# if age.isnumeric():
#     age = int(age)
#     if age >= 18:
#         print(f'You are adult. Your age is {age}')
#     else:
#         print(f'You are young. Your age is {age}')
# else:
#     print('ERROR: Try again with digits')
# print('End.')

# ===================== Iteration/cycle

# x = 4
# while x:
#     print(x)
#     if x == 10:
#         x = 0
#     else:
#         x += 1
# print(x)

# x = 0
# while x <= 100:
#     if x % 5 == 0:
#         print(x)
#     x += 1
    
# x = 100
# while x >= 0:
#     if not x % 5:
#         print(x)
#     x -= 1

# ===================== for ... in ...

# lst = [1, 2, 3, 4] #type list

# for item in lst:
#     print(item)

# for item in lst:
#     print('what it will be?')

# hello = 'Hi, there'
# for symbol in hello:
#     print(symbol)

# entered_text = input('Enter some text: ')
# for symbol in entered_text:
#     if symbol == ' ':
#         print('you have a space here')
#     if symbol.isdigit():
#         print('you have a digit here')

# print(entered_text)
# print(entered_text.split())

# for word in entered_text.split():
#     print(word)

# phrase = 'our text for test'
# for _ in phrase: # _ - ignor variable 
#     print('some new text')

# ===================== for ... in ...+ range()

# for i in range(10):
#     print(i)

# for i in range(3, 10):
#     print(i)

# for i in range(1, 10, 4):
#     print(i)

# ===================== continue / break

# numbers = [2, 1, 3, 4, 6, 8 , 9, 12]
# for i in numbers:
#     if i % 2:
#         continue
#     print(i)

# text = 'Hello, world!'
# i = 0
# while i < len(text):
#     if text[i] == 'o':
#         print(f'Index of the "o" letter is {i}')
#         break
#     print(f'Letter at the {i} position is not "o"')
#     i += 1

# for i in range(1, 10):
#     if i % 2:
#         continue
#     print(i)

# for i in range(10):
#     if i > 5:
#         break
#     print(i)

# x = 1
# while x < 25:
#     if x == 7:
#         break
#     if x % 2:
#         print('odd')
#     else: 
#         print('even')
#     x += 1

# while True:
#     command = input("Enter a command: ")
#     if command == "name":
#         print('Name is Oleg')
#     elif command == 'exit':
#         print('exiting')
#         break
#     else:
#         print(f'Command `{command}` not found. Available commands:\n'
#               f'name: print a name\n'
#               f'exit: stop the program')
# print("Good bye!")

# ===================== FUNCTIONS

# def my_function():
#     print('Hello function!!!')
# my_function()

# def my_function1(argument):
#     print(f'Hello function!!! My Argument is - {argument}')
# my_function1('TRUE') 

# def my_function2(a, b):
#     return a + b
# my_sum = my_function2(7, 4)
# print(my_sum)

# === return function ===

# def test():
#     def inner_test():
#         print('inner function text')
#     return 1, inner_test

# number, func = test()
# print(number)
# func()

# def mult_return():
#     return 1, 2
# one, two = mult_return()

# print(one, two)

# def my_func():
#     return 1

# def my_void_func():
#     a = 1
#     a += 1

# a = my_func()
# b = my_void_func()

# print(a, b)

# def default_args(a = 1, b = 2, c = 3):
#     print(a, b, c)
# default_args(b = 7)

# def test_args(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)

# lst = [1, 2, 3]
# test_args(*lst)

# def test_args(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)

# dct = {"arg3": 1, "arg2": "two", "arg1": 3}
# test_args(**dct)


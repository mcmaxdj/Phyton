# === Functions - second part ===

# def my_func(first_arg, a = 1, b = 1, c = 1):
#     print(first_arg, a, b, c)
# my_func(5, 4)

# def my_args_func(*args):
#     print(args)
# my_args_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def my_kwargs_func(**kwargs):
#     print(kwargs)
# my_kwargs_func(first = 1, second = 2, third = 3)
# {'first': 1, 'second': 2, 'third': 3}

# def my_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# my_func(1, 2, 3, first = 1, second = 2, third = 3)
# (1, 2, 3)
# {'first': 1, 'second': 2, 'third': 3}

# def my_func(name, age, *args, **kwargs):
#     print(name, age)
#     print(args)
#     print(kwargs)
# my_func('Maks', 21, 'Male', city='Kharkiv', country='Ukraine')
# Maks 21
# ('Male',)
# {'city': 'Kharkiv', 'country': 'Ukraine'}

# def my_func(*my_test, **another_test):
#     print(my_test)
#     print(another_test)
# my_func(1, 2, 3, first = 4, second = 5, third = 6)
# (1, 2, 3)
# {'first': 4, 'second': 5, 'third': 6}

# def my_func(*args):
#     for item in args:
#         print(f'{item} - type: {type(item)}')
# my_func('Hey', 1, 1.23, True, 2, 3, 'World')

# def my_super_func(name, age, *args, city = "Kyiv", **kwargs):
#     print(name, age, args, city, kwargs)
# my_super_func('Max', 21, city = 'Kyiv')
# Max 21 () Kyiv {}

# def my_func(name, age, **kwargs):
#     user = f"Username: {name}, Age: {age}"
#     if 'phone' in kwargs:
#         user += f", Phone: {kwargs.get('phone')}"
#     print(user)

# my_func('Max', 32)
# my_func('Max', 32, phone = 48516062260)

# === HIGHER-ORDER FUNCTIONS (Функции высшего порядка) ===
"""
:принимают как аргументы:
:другие функции или возвращают:
:ругую функцию как результат:
"""

# def modify(f, a):
#     return f(a)

# def text_to_upper(s):
#     return s.upper()

# print(modify(text_to_upper, 'some new text to upper'))

# ============

# data = [1, 2, 3]
# def multiply_by_2(number):
#     return number * 2
# print([i for i in map(multiply_by_2, data)])

# ============ CLOSURES (Замыкания) ============

# def closure(message):
#     def print_message():
#         print(message)
#     return print_message

# print_hi = closure('Hiiiii!')
# print_hi()
# print_yes = closure('Yeeeeees!')
# print_yes()

# ============ LAMBDA (Функции не имеющие имен) ============

# my_lambda = lambda x: x * 2
# result = my_lambda(3)
# print(result)

# data = [1, 2, 3]
# print([i for i in map(lambda x: x * 2, data)])
# [2, 4, 6]

# words = ['I', 'Love', 'Programming', 'Language', 'Python']
# print(sorted(words, key = lambda x: len(x)))
# ['I', 'Love', 'Python', 'Language', 'Programming']

# ============ Practice ============

# def modify(modifier, data):
#     return modifier(data)

# def power(number):
#     return number ** 2

# def add_2(number):
#     return number + 2

# res = modify(lambda number: number * 4, 7) # lambda
# lmd = lambda x, y: x + y
# res = lmd(1, 2)
# print(res)

# res = modify(power, 10)
# print(res)
# print(modify(add_2, 3))

# words = ['I', 'Love', 'to', 'be', 'the', 'a', 'one']
# print(sorted(words))
# print(sorted(words, key=lambda x: len(x) * -1))
# ['I', 'Love', 'a', 'be', 'one', 'the', 'to']
# ['Love', 'the', 'one', 'to', 'be', 'I', 'a']

# def printer(text):
#     def my_print():
#         print(text)
#     return my_print
# print_hello = printer('hello')
# print_test = printer('test')
# print_hi = printer('hi')
# print_hello()
# print_test()
# print_hi()

# ============ ENTRYPOINT (точка входа) ============

# def second_test():
#     print('test')

# def test():
#     print('its me')

# def main():
#     test()
#     second_test()

# if __name__ == "__main__":
#     main()


# ===== Data types =====
# =====    LIST    =====

# lst = []
# new_lst = list()
# lst_with_data = ['test', True, 123, lst]
# new_lst_with_data = list([1, 2, 3])

# list methods
"""
list - reserved name (can't be used like a variable)
.append     - add new element to the end of the list
.extend     - merge 2 lists in one
lst1 + lst2 - connect 2 lists
.remove     - remove elements
    del     - remove elements
item in lst - check if the value is in the list
"""

# empty_list = []
# res = empty_list.append(1)
# for i in range(10):
#     empty_list.append(i)

# print(empty_list)
# empty_list.insert(12, 42)
# print(empty_list)
# if 1 in empty_list:
#     empty_list.remove(1)
# print(empty_list)

# ===== =====
# new_list = list()
# print(new_list)

# my_string = 'some text@ !'
# my_string_in_list = list(my_string)
# print(my_string_in_list)

# ===== =====
# int_in_list = list()
# int_in_list.append(1)
# int_in_list.append(3)
# print(int_in_list)

# ===== =====
# existing_list1 = ['apple', 'banana', 1, 2, 3]
# existing_list2 = ['BMW', True, 5, 6, 7]
# existing_list1.extend(existing_list2)
# existing_list1.append(existing_list2)
# print(existing_list1)

# ===== =====
# while 1 in existing_list1:
#     existing_list1.remove(1)
# print(existing_list1)

# empty_lst = [2, 3, 4, 5, 6, 7, 8, 1, 9]
# i = 0
# while i < len(empty_lst):
#     if empty_lst[i] == 1:
#         del empty_lst[i]
#     else:
#         i += 1
# print(empty_lst)

# ===== =====
# empty_list = list([2, 3, 4, 5, 12])
# print(empty_list[0])

# for item in empty_list:
#     print(item)

# print(empty_list[-2])
# print(empty_list[len(empty_list) - 1])

# =====    TUPLE    =====

# tuple = (1, 2, 3)
# new_tuple = tuple([1, 2, 3])
"""
can contain diferent types of data,
this data can't be changed
"""

# def my_tuple():
#     return 1, 2, 3
# print(my_tuple())

# =====
# my_list = [1, 2, 3]
# my_tuple = (4, 5, 6)

# my_list[0] = 'test'
# print(my_list)
# my_tuple[0] = 'milk'
# print(my_tuple)

# =====
# my_tuple = ([], 2, 3)
# print(my_tuple)
# my_tuple[0].append('krocs')
# print(my_tuple)

# =====
# my_tuple = (1, 2, 3, 4)
# my_list = list(my_tuple)
# print(my_list)
# my_list.append(True)
# print(my_list)

# =====    SLICE    =====
"""
[start: end: step]
start - from what place we will start. 0 - by default
end (index) - which element will be place. not be included in collection
step - by default = 1
1 - take every element from START to END
2 - take every second element
'-' - start from the end of the collection
[:-1] - collection from before last element (-1 - 1 = -2)
[:2] - collection from third element
[1:5:2] - collection from secont to fifth element with step two
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lst[1:] -> [1, 2, 3, 4, 5, 6, 7, 8]
lst[1:-1] -> [1, 2, 3, 4, 5, 6, 7]
lst[1:5:2] -> [1, 3]
lst[1:7:2] -> [1, 3, 5]
lst[1:7:3] -> [1, 4]
lst[::-1] -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
# =====    Functions to work with data-types, collections    =====

# MAP
# def multiply(number):
#     return number * 2
# lst = [1, 2, 3]
# for item in map(multiply, lst):
#     print(item)

# REDUCE
# lst = [2, 3, 4]
# func = lambda a, b: a + b
# lst_sum = reduce(func, lst)

# FILTER
# lst = [1, 2, 3, 4, 5, 6]
# res = filter(lambda a: a % 2, lst)
# for item in res:
#     print(item)

# ZIP
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# for item in zip(lst1, lst2):
#     print(item)

# SORTED

# dict, set, frozenset, comprehension
# dct = {}
# new_dct = dict()
# dct_with_data = {'key': 'value', 'new_key': 'new value for the new_key'}

# spends = {'food': 500, 'car': 200, 'education': 100}
# spends['food'] # 500
# spends.get('food') # 500
# spends['travel'] # error
# spends.get('travel') #None

# spends['travel'] = 0
# spends.get('travel') # 0

# spends['travel'] = 100
# spends.get('travel') # 100
# spends['travel'] += 100
# spends.get('travel') # 200
# spends['travel'] = 0
# spends.get('travel') # 0

# ==== ==== ==== ==== ====
# my_dict = dict()

# my_key = input('Enter the key: ')
# my_value = input('Enter a value: ')

# my_dict[my_key] = my_value
# my_dict['age'] = input('Enter your age: ')
# print(my_dict)

# ==== ==== ==== ==== ====
# my_dict = dict()
# my_key = 'name'
# my_value = 'Olek'

# my_dict[my_key] = my_value
# my_dict['age'] = 32

# print(my_dict['name'])
# print(my_dict.get('test'))

# if 'age' in my_dict:
#     print(my_dict['age'])
# else:
#     print('Test does not exist')

# my_dict['test'] = 'test value'
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())
# print(list(my_dict.values()))
# print(my_dict.items())

# for item in my_dict.items():
#     print(item)

# for key, value in my_dict.items():
#     if key == 'name':
#         print(value.upper())
#     else:
#         print(value)

# ==== ==== ==== ==== ==== 
# set - can contain only uniq data
# my_set = {1, 2, 3}
# new_set = set([1, 2, 3]) # revert list to set
# new_uniq_set = set([1, 1, 2, 2]) # {1, 2} - getting uniq data from list

# my_set.add(4)
# my_set.remove(1)

# new_set = {4, 5, 6}

# my_set & new_set # can find all dublicated elems in two sets
# my_set | new_set # return new set with firs and second sets inside
# my_set.pop() # get first elem from set and remove it

# f_set = frozenset([1, 2, 3]) # can't add or remove elems

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)

# my_first_set = {1, 2, 3, 4, 5}
# my_second_set = {1, 3, 5, 7, 9}
# print(my_first_set & my_second_set)
# print(my_first_set.intersection(my_second_set))
# print(my_first_set | my_second_set)
# print(my_first_set.union(my_second_set))
# print(my_first_set.difference(my_second_set))
# print(my_first_set - my_second_set)
# print(my_first_set ^ my_second_set)
# print(my_first_set.symmetric_difference(my_second_set))

# lst = [1, 2, 3, 4, 3, 2, 1, 4, 5, 6, 7, 7]
# new_lst = list(set(lst))
# print(new_lst)

# ==== ==== ==== ==== ==== 
# list comprehension: [n for n in range(5)] -> [0, 1, 2, 3, 4]
# dict comprehension: {n: f"value of {n}" for in range(2)} -> {0: "value of 0", 1: "value of 1"}
# set comprehension: {n for n in range(5)} -> {0, 1, 2, 3, 4}

# lst = [1, 2, 3, 4, 5]
# print(set(lst))

# my_set = {n * 2 for n in lst}
# print(my_set)
# my_set = {f'string {n}' for n in lst}
# print(my_set)

# my_dict = {f'key-{n}': 'value' for n in lst}
# print(my_dict)

import random
my_random_list = [random.randint(0, 100) for _ in range(7)]
print(my_random_list)
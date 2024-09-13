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


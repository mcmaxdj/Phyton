# === Classes ===

# class Test:
#     number = 1 # class attribute

#     def print_number(self): # class method
#         print(self.number)

# test_obj = Test() # class instance
# test_obj.print_number() # calling of class method
# print(test_obj.number) # accessing to class attribute

# ===  ===

# class MyParentClass:
#     name = "Maksym" # class attribute

#     def print_name(self): # class method
#         print(self.name)

# class MyChildClass(MyParentClass): # inheritance
#     name = "Loki" # class attribute

# ===  ===

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# first_point = Point(0, 0) # create an instance of Point class
# second_point = Point(10, 10) # create an instance of Point class

# print(first_point.x, first_point.y, second_point.x, second_point.y)

# ===  ===

# class Rectangle:
#     def __init__(self, a, b):
#         self.slide_a = a
#         self.slide_b = b

#     def get_square(self):
#         return self.slide_a * self.slide_b
    
#     def get_perimeter(self):
#         return (self.slide_a + self.slide_b) * 2
    
# rect1 = Rectangle(10, 7)
# rect2 = Rectangle(12, 8)

# if rect1.get_square() > rect2.get_square():
#     print('First rect is bigger then second')
# else:
#     print('Second rect is bigger then first or they are the same')

# ===  ===

# class Car:
#     wheel = 4
#     fuel = 40
#     def move(self, kilometers):
#         self.fuel -= kilometers * 0.1

# my_car = Car()
# my_wife_car = Car()

# # print(my_car.fuel)
# # my_car.move(15)
# # print(my_car.fuel)

# class Truck(Car):
#     fuel = 100
#     def move(self, kilometers):
#         self.fuel -= kilometers * 0.3

# truck = Truck()
# print(truck.wheel)

# === how to create class (3 ways) ===

# class MyOrder:
#     pass

# class MyNewOrder(object):
#     pass

# class MyLastOrder():
#     pass

# ===  ===

# class MyOrder:
#     number = 'qwerty1234'

#     def __init__(self, amount):
#         self.amount = amount

# order = MyOrder(100)
# print(order.number, order.amount)

# === self ===

# class MyOrder:
#     def __init__(self, amount):
#         self.amount = amount
#         self.is_payd = False

#     def pay(self):
#         self.is_payd = True

#     def print_self(self):
#         print(self)

# order = MyOrder(100)
# order2 = MyOrder(200)
# order.pay()

# print(order.is_payd, order2.is_payd)
# order2.pay()
# print(order.is_payd, order2.is_payd)

# print(order)
# order.print_self()

# === parent classes ===

# class MyOrder:
#     def __init__(self, amount):
#         self.amount = amount
#         self.is_payd = False

#     def pay(self):
#         self.is_payd = True

#     def print_amount(self):
#         print(self.amount)

# order = MyOrder(100)
# print(order.amount)

# class MyOrderChild(MyOrder):
#     def pay(self):
#         if self.amount > 100:
#             self.is_payd = True
#         else:
#             print('Not anough money')

# order = MyOrderChild(100)
# print(order.is_payd)
# order.pay()
# print(order.is_payd)

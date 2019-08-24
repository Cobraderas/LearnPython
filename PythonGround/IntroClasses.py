# create a Animal class
# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#
#
# zebra = Animal("Jeff")
# print(zebra.name)

# ==============================================================

# Class definition
# class Animal(object):
#     """Makes cute animals."""
#     # For initializing our instance objects
#     def __init__(self, name, age, is_hungry):
#         self.name = name
#         self.age = age
#         self.is_hungry = is_hungry
#
# # Note that self is only used in the __init__()
# # function definition; we don't need to pass it
# # to our instance objects.
#
#
# zebra = Animal("Jeffrey", 2, True)
# giraffe = Animal("Bruce", 1, False)
# panda = Animal("Chad", 7, True)
#
# print(zebra.name, zebra.age, zebra.is_hungry)
# print(giraffe.name, giraffe.age, giraffe.is_hungry)
# print(panda.name, panda.age, panda.is_hungry)


# CLASS SCOPE
# """
# each individual animal gets its own name and age
# (since they’re all initialized individually),
# but they all have access to the member variable is_alive,
# since they’re all members of the Animal class
# """


# class Animal(object):
#     """Makes cute animals."""
#     is_alive = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# zebra = Animal("Jeffrey", 2)
# giraffe = Animal("Bruce", 1)
# panda = Animal("Chad", 7)
#
# print(zebra.name, zebra.age, zebra.is_alive)
# print(giraffe.name, giraffe.age, giraffe.is_alive)
# print(panda.name, panda.age, panda.is_alive)


# class Animal(object):
#     """Makes cute animals."""
#     is_alive = True
#     health = "good"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # Add your method here!
#     def description(self):
#         print(self.name)
#         print(self.age)
#
#
# hippo = Animal("Crocodile", 36)
# hippo.description()
# sloth = Animal("Ciupacabra", 2)
# ocelot = Animal("Cioara", 80)
#
# print(hippo.health)
# print(sloth.health)
# print(ocelot.health)


# class ShoppingCart(object):
#     """Creates shopping cart objects
#         for users of our fine website."""
#     items_in_cart = {}
#
#     def __init__(self, customer_name):
#         self.customer_name = customer_name
#
#     def add_item(self, product, price):
#         """Add product to the cart."""
#         if product not in self.items_in_cart:
#             self.items_in_cart[product] = price
#             print(product + " added.")
#         else:
#             print(product + " is already in the cart.")
#
#     def remove_item(self, product):
#         """Remove product from the cart."""
#         if product in self.items_in_cart:
#             del self.items_in_cart[product]
#             print(product + " removed.")
#         else:
#             print(product + " is not in the cart.")
#
#
# my_cart = ShoppingCart("Ion")
# my_cart.add_item("morcovi", 5)
# my_cart.remove_item("morcovi")


# """Inheritance concepts"""


# class Customer(object):
#     """Produces objects that represent customers."""
#     def __init__(self, customer_id):
#         self.customer_id = customer_id
#
#     def display_cart(self):
#         print("I'm a string that stands in for the contents of your shopping cart!")
#
#
# class ReturningCustomer(Customer):
#     """For customers of the repeat variety."""
#     def display_order_history(self):
#         print("I'm a string that stands in for your order history!")
#
#
# monty_python = ReturningCustomer("ID: 12345")
# monty_python.display_cart()
# monty_python.display_order_history()
#
# """defined a class, Customer, as well as a ReturningCustomer
# class that inherits from Customer. Note that we don’t define
# the display_cart method in the body of ReturningCustomer,
# but it will still have access to that method via inheritance"""


# class Shape(object):
#     """Makes shapes!"""
#     def __init__(self, number_of_sides):
#         self.number_of_sides = number_of_sides
#
#
# # Add your Triangle class below!
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3


# class Employee(object):
#     """Models real-life employees!"""
#     def __init__(self, employee_name):
#         self.employee_name = employee_name
#
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 20.00
#
#
# # Add your code below!
# class PartTimeEmployee(Employee):
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 12.00
#
#     def full_time_wage(self, hours):
#         return super(PartTimeEmployee, self).calculate_wage(hours)
#
#
# milton = PartTimeEmployee("Morcov")
# print(milton.full_time_wage(10))


# class Triangle(object):
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#
#     number_of_sides = 3
#
#     def check_angles(self):
#         if self.angle1 + self.angle2 + self.angle3 == 180:
#             return True
#         else:
#             return False
#
#
# my_triangle = Triangle(90, 30, 60)
# print(my_triangle.number_of_sides)
# print(my_triangle.check_angles())
#
#
# class Equilateral(Triangle):
#     angle = 60
#
#     def __init__(self):
#         self.angle1 = self.angle
#         self.angle2 = self.angle
#         self.angle3 = self.angle
#
#
# my_Equilateral = Equilateral()
# print(my_Equilateral.number_of_sides)
# print(my_Equilateral.check_angles())



# vazifa 1
# class MyValueError(Exception):
#     pass
#
#
# class Descriptor:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name)
#
#     def __set__(self, instance, value):
#         if isinstance(value, str):
#             instance.__dict__[self.name] = value.lower()
#         else:
#             raise MyValueError("Qiymat faqat string bo'lishi kerak.")
#
#     def __delete__(self, instance):
#         if self.name in instance.__dict__:
#             del instance.__dict__[self.name]
#         else:
#             raise MyValueError(f"{self.name} atributi yo'q.")
#
#
# class Person:
#     name = Descriptor("name")
#     lastname = Descriptor("lastname")
#
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#
# class Cars:
#     cars = Descriptor("car_name")
#     def __init__(self, car_name):
#         self.car_name = car_name
#
#
# try:
#     person = Person("Asilbek", "Odiljonov", 18)
#     car = Cars("malibu")
#     print(person.name)
#     print(person.lastname)
#     print(person.age)
#     print(car.cars)
# except MyValueError as e:
#     print(e)

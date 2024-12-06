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

# ===============================================================

# vazifa 2
# class MyValueError(Exception):
#     pass
#
# class NumberDescriptor:
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name)
#
#     def __set__(self, instance, value):
#         if value > 0:
#             instance.__dict__[self.name] = value
#         else:
#             raise MyValueError("Musbat son kiritin!!!")
#
#     def __delete__(self, instance):
#         if self.name in instance.__dict__:
#             del instance.__dict__[self.name]
#         else:
#             raise MyValueError(f"{self.name} atributi yo'q.")
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#
# class Number:
#     num = NumberDescriptor()
#
#     def __init__(self, num):
#         self.num = num
#
# try:
#     num1 = int(input("son kiritin: "))
#     num = Number(num1)
#     print(num.num)
# except MyValueError as e:
#     print(e)

# ===============================================================

# vazifa 3
from datetime import datetime, timedelta
#
#
# while True:
#     commond = input("Buyruqni kiritin (help -> yordam): ").lower()
#     if commond == "stop":
#         print("Dastur toxtatildi!!!")
#         break
#     elif commond == "bugun":
#         bugun = datetime.now()
#         print(f"Bugungi sana {bugun.strftime("%Y-%m-%d")}")
#         break
#     elif commond == "oldin":
#         oldin = datetime.now() - timedelta(days=7)
#         print(f"7 kun oldingi sana {oldin.strftime("%Y-%m-%d")}")
#         break
#     elif commond == "keyin":
#         keyin = datetime.now() + timedelta(days=7)
#         print(f"7 kun keyingi sana {keyin.strftime("%Y-%m-%d")}")
#         break
#     elif commond == "help":
#         print(
#             """ stop ->  toxtatish\n help ->  yordam\n bubun ->  bugungi sana\n keyin ->  7kun keyingi sana\n oldin ->  7kun oldingi sana\n"""
#         )

# ===============================================================

# vazifa 4
# from datetime import datetime
# try:
#     tugilgan_yil = int(input("Tugilga yilingizni kiritin(YYYY -> formatta): "))
#     tugilgan_oy = int(input("Tugilga oyingizni kiritin(MM -> formatta): "))
#     tugilgan_kun = int(input("Tugilga kuningizni kiritin(DD -> formatta): "))
#     bugun = datetime.now()
#     tugilgan_sana = datetime(tugilgan_yil, tugilgan_oy, tugilgan_kun)
#     yosh = bugun.year - tugilgan_sana.year
#     if (bugun.month, bugun.day) == (tugilgan_sana.month, tugilgan_sana.day):
#         print("Tugilgan kiniz blan🥳🥳🥳")
#     else:
#         print(yosh," yosh")
# except ValueError as e:
#     print(e)
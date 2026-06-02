# class Gaari:
#     def __init__(self, brand):
#         self.brand = brand
#
# class Baabuur(Gaari): # Halkan ku qor class-ka uu ka dhaxlayo
#     def dhex_soco(self):
#         print(f"Baabuurka {self.brand} waa uu socdaa.") # Halkan ku qor variable-ka magaca
#
# # Tijaabi
# toyota = Baabuur("Toyota")
#
# toyota.dhex_soco()
#
#
#
#
#
#
#
# # Adigoo isticmaalaya koodhkii hore ee Animal, samee class cusub oo la yiraahdo Cat.
# #
# # Cat waa inuu ka dhaxlaa Animal.
# #
# # Waa inuu leeyahay shaqo (method) la yiraahdo meow.
# #
# # Marka la waco meow, waa inuu daabacaa: "Magaca_Bisadda says Meow!".
#
#
# class Animal:
#     def __init__(self, name):
#         self.name=name
#
#     def info(self):
#         print("xaywaakan",self.name)
#
# class Cat(Animal):
#     def meow(self):
#         print(self.name,'waxa uu leeyahay: meow meow')
#
# c=Cat("sacad")
#
#
#
# c.info()
# c.meow()

#
# class Employee:
#     # 1. Waxaa la saxay __init__ (Laba hoos-ka-xariiq oo labada dhinac ah)
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def info(self):
#         print(f"magaciisu waa:{self.name}, musahrkiisuna waa:{self.salary}")
# class Manager(Employee):
#     def calculate_bonus(self):
#         gunno = self.salary * 0.1
#         # 2. Waxaa la saxay f-string-ka si uu u daabaco gunnada si nadiif ah
#         print(f"Maareeye {self.name}, gunnadaadu waa: ${gunno}")
#
# # 3. Tijaabinta
# m = Manager("Qorsheeye", 1000)
#
# m.info()
# m.calculate_bonus()


# Parent Class: Samee class la yiraahdo Gaadhi oo leh sifo ah sumad (brand).
#
# Child Class: Samee class la yiraahdo ElectricCar oo dhaxlaya Gaadhi.
#
# Super: Isticmaal super() si uu waalidku u kaydiyo sumad,
# ilmahuna u kaydiyo sifo cusub oo ah battery_size.

# class Gaadhi:
#     def __init__(self, brand):
#         self.brand = brand
#
# class ElectricCar(Gaadhi):
#     def __init__(self, brand, battery_size):
#         super().__init__(brand)
#         self.battery_size = battery_size # (Halkan waxaan u yara dhignay xaraf yar 's')
#
# # Samaynta Object-ga
# S = ElectricCar("Toyota", "500V")
#
# # Aan hubino xogta
# print(f"Gaadhigani waa: {S.brand}")
# print(f"Batarigiisu waa: {S.battery_size}")




































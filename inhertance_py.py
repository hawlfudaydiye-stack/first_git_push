# # # 1. Qeexidda Class-ka waalidka ah (Parent Class)
# # # Class-kani waa naqshadda guud ee xayawaan kasta yeelan karo.
# # class Animal:
# #     # __init__ waa 'constructor' - shaqadiisu waa inuu diyaariyo sifooyinka bilowga ah
# #     def __init__(self, name):
# #         self.name = name  # Halkan waxaa lagu kaydiyaa magaca xayawaanka
# #
# #     # info waa 'method' (shaqo) soo daabacaysa macluumaadka xayawaanka
# #     def info(self):
# #         print("Animal name:", self.name)
# #
# #
# # # 2. Qeexidda Class-ka ilmaha ah (Child Class)
# # # 'Dog(Animal)' waxay ka dhigan tahay in Dog uu dhaxlayo wax kasta oo Animal lahaa.
# # class Dog(Animal):
# #     # sound waa shaqo u gaar ah eeyga (Dog), oo uusan lahayn waalidku
# #     def sound(self):
# #         print(self.name, "barks")
# #
# #
# # # 3. Sameynta 'Object' (Tusaale dhab ah)
# # # Waxaan abuuraynaa eey la yiraahdo "Buddy".
# # # Inkastoo Dog uusan lahayn __init__, wuxuu ka soo amaahanayaa waalidka (Animal).
# # d = Dog("Buddy")
# #
# # # 4. Wicitaanka Shaqooyinka (Methods)
# # # d.info() waxay u yeeraysaa shaqadii uu ka dhaxlay waalidka.
# # d.sound()
# # d.info()
# #
# # # d.sound() waxay u yeeraysaa shaqada isaga u gaarka ah ee lagu dhex qoray Dog.
#
# # 1. Waalidka (Parent Class)
# class Animal:
#     def __init__(self, name, color):
#         self.name = name  # Halkan waxaa lagu kaydiyaa Magaca
#         self.color = color  # Halkan waxaa lagu kaydiyaa Midabka
#
#     def info(self):
#         print(f"Magaca: {self.name}, Midabka: {self.color}")
#
#
# # 2. Ilmaha (Child Class)
# class Dog(Animal):
#     def sound(self):
#         # Halkan waxaan ku wada isticmaalaynaa Magaca iyo Midabka
#         print(f"{self.name} oo ah eey {self.color} ah, wuxuu leeyahay: 'Woof Woof!'")
#
#
# # 3. Tijaabinta (Abuurista Object leh labo sifo)
# d = Dog("Buddy", "Madow")
#
# # Shaqooyinka aan wacno
# d.info()  # Waxay soo saartaa: Magaca: Buddy, Midabka: Madow
# d.sound()  # Waxay soo saartaa: Buddy oo ah eey Madow ah, wuxuu leeyahay: 'Woof Woof!'





#
# Adigoo isticmaalaya koodhkii hore ee Animal, samee class cusub oo la yiraahdo Cat.
#
# Cat waa inuu ka dhaxlaa Animal.
#
# Waa inuu leeyahay shaqo (method) la yiraahdo meow.
#
# Marka la waco meow, waa inuu daabacaa: "Magaca_Bisadda says Meow!".


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


# 1. Waalidka (Parent Class)
class Xayawaan:
    def __init__(self, magac):
        self.magac = magac
        print(f"--- {self.magac} xogtadiisa waa la bilaabay ---")


# 2. Ilmaha (Child Class)
class Bisad(Xayawaan):
    def __init__(self, magac, midab):
        # super() waxay u yeeraysaa waalidka si uu 'magac' u habeeyo
        super().__init__(magac)

        # Midabkan bisadda unbaa iska leh
        self.midab = midab
        print(f"--- Midabka {self.midab} ah waa lagu daray ---")

    def hadal(self):
        print(f"{self.magac} oo {self.midab} ah ayaa leh: Meow!")


# --- TIJAABADA ---
bisad1 = Bisad("Muraayad", "Caddaan")
bisad1.hadal()







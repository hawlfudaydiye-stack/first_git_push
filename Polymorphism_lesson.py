#
#
#
# ""
"""
examples kan oo dhan oo hoose waa qayb kamid ah polymorphismoo ladhaho
A) Compile-time Polymorphism (Method Overloading)

"""
#
#
# class Xisaabiye:
#     # Waxaan isticmaalaynaa 'None' si aan u dhibno in paramenter-ku uu madhan yahay
#     def bedka(self, a=None, b=None):
#
#         # 1. Haddii 'a' iyo 'b' labadaba la soo dhiibo (Rectangle)
#         if a is not None and b is not None:
#             print(f"Bedka Rectangle-ka waa: {a * b}")
#
#         # 2. Haddii 'a' kaliya la soo dhiibo (Square)
#         elif a is not None:
#             print(f"Bedka Square-ka waa: {a * a}")
#
#         # 3. Haddii aan waxba la soo dhiibin
#         else:
#             print("Fadlan soo geli ugu yaraan hal nambar!")
#
#
# # --- ISTICMAALKA ---
# obj = Xisaabiye()
#
# obj.bedka(5)  # Waxay soo saaraysaa: 25 (Square)
# obj.bedka(5, 10)  # Waxay soo saaraysaa: 50 (Rectangle)
# obj.bedka()
#
# class SalaanHelper:
#     def dheh_haye(self, magaca, xilliga=None):
#         if xilliga is not None:
#             print(f"{magaca} , {xilliga} wanaagsan!")
#         else:
#             print(f"Haye {magaca}!")
#
# # --- Isticmaalka ---
# obj = SalaanHelper()
#
# obj.dheh_haye("Ahmed")                # Output: Haye Ahmed!
# obj.dheh_haye("Sahra", "Galab")       # Output: Galab wanaagsan, Sahra!



# class Xisaabiye:
#     def isku_dar(self, a, b, c=None):
#         if c is not None:
#             natiijo = a + b + c
#             print(f"Isku-darka 3-da nambar waa: {natiijo}")
#         else:
#             natiijo = a + b
#             print(f"Isku-darka 2-da nambar waa: {natiijo}")
#
# # --- Isticmaalka ---
# calc = Xisaabiye()
#
# calc.isku_dar(10, 20)          # Output: 30
# calc.isku_dar(10, 20, 30)      # Output: 60

"""
examples kan oo dhan oo hoose waa qayb kamid ah polymorphismoo ladhaho
B) Method Overriding? (Runtime Polymorphism)

"""
#
# class Xayawaan:
#     def dhawaaq(self):
#         print("Xayawaanku dhawaaq buu leeyahay")
#
# class Eey(Xayawaan):
#     # Halkan ayaan ku samaynay OVERRIDING (Waxaan beddelnay shaqadii aabaha)
#     def dhawaaq(self):
#         print("Eeygu wuxuu dhahaa: Wuff Wuff!")
#
# class Bisad(Xayawaan):
#     # Halkan isna Override baa ka dhacay
#     def dhawaaq(self):
#         print("Bisadu waxay dhahdaa: Meow Meow!")
#
# # --- ISTICMAALKA (Runtime) ---
# xayawaanada = [Eey(), Bisad(),Xayawaan()]
#
# for x in xayawaanada:
#     x.dhawaaq() # Halkan Python waxay go'aaminaysaa dhawaaqa saxda ah xilliga uu koodhku socdo
#

#
# # Waalidka
# class Shaqaale:
#     def shaqada(self):
#         return "Shaqo guud ayuu qabtaa"
#
# # Ilmaha 1
# class Maamule(Shaqaale):
#     def shaqada(self):
#         return "Xafiiska ayuu maamulaa 💻" # Wuu beddelay shaqadii waalidka
#
# # Ilmaha 2
# class Nadiifiye(Shaqaale):
#     def shaqada(self):
#         return "Xafiisyada ayuu nadiifiyaa 🧹" # Wuu beddelay shaqadii waalidka
#
# # -- Tijaabada Polymorphism-ka --
# dad = [Maamule(), Nadiifiye(), Shaqaale()]
#
# for qof in dad:
#     # Hal magac (shaqada) laakiin 3 ficil oo kala duwan!
#     print(qof.shaqada())




"""
examples kan oo dhan oo hoose waa qayb kamid ah polymorphismoo ladhaho
c) Ducktyping

"""

#
# class Shimbir:
#     def duul(self):
#         return "Baalal ayay ku duulaysaa 🦅"
#
# class Diyaarad:
#     def duul(self):
#         return "Matoor ayay ku duulaysaa ✈️"
#
# # Kani waa Function-ka dhexdhexaadka ah
# # Ma xiiseeyo inuu shaygu nool yahay iyo inuu mashiin yahay
# def tijaabi_duulista(shay):
#     print(shay.duul())
#
# # -- Tijaabada Duck Typing --
# tijaabi_duulista(Shimbir())   # Wuxuu qabanayaa shaqada Shimbirta
# tijaabi_duulista(Diyaarad())  # Wuxuu qabanayaa shaqada Diyaaradda


"""
examples kan oo dhan oo hoose waa qayb kamid ah polymorphismoo ladhaho
d) Polymorphism-ka Luuqadda Ku Dhex Jira (Built-in / Operator Polymorphism) 
"""

# 1. Tusaalaha Calaamadda (+)
print(5 + 10)                  # Natiijadu waa 15 (Xisaab isku-dar ah)
print("Biyo " + "Macaan")      # Natiijadu waa "Biyo Macaan" (Qoraal isku-dhejin ah)
print([1, 2] + [3, 4])         # Natiijadu waa [1, 2, 3, 4] (Liis isku-dar ah)

# 2. Tusaalaha Shaqada len()
print(len("Soomaaliya"))       # Wuxuu soo celinayaa 10 (Inta xaraf ee ku jirta)
print(len(["Tufaax", "Moos"])) # Wuxuu soo celinayaa 2 (Inta xabbadood ee liiska ku jirta)
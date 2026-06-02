
# s = "GFG"
# it = iter(s) # Waxaan ka dhignay Iterator
#
# print(next(it)) # Natiijadu: G
# print(next(it)) # Natiijadu: F
# print(next(it)) # Natiijadu: G

# Tani waa meesha ay ku kala duwan yihiin adiga iyo For Loop-ka.
# Haddii aad mar 4-aad dhahdo print(next(it)), Python waxay ku siinaysaa Error la yidhaahdo StopIteration.
# print(next(it))
# sababtuna waa in for loop aotumatic isga yahya oo markiiba si aotumatic ah u istaago
#haka iteroter ku uu yahay manual oo larabo in aad adigu istaajiso

# class EvenNumbers:
#     def __iter__(self):
#         self.n = 2  # Waxaan ka bilaabaynaa 2
#         return self
#
#     def __next__(self):
#         x = self.n
#         self.n += 2  # Mar kasta 2 ku dar si uu u noqdo Even
#         return x
#
# # Isticmaalka
# even = EvenNumbers()
# it = iter(even)
#
# print(next(it)) # 2
# print(next(it)) # 4
# print(next(it)) # 6




# Layliga 1
# asxaabta = ["Cali", "Faarax", "Hani", "Deeqa"]
# # Halkan ka sii wad...
# it = iter(asxaabta)
# print(next(it))
# print(next(it))
# print(next(it))


#
# # Layliga 2
# class Dhimis:
#     def __iter__(self):
#         self.n=10
#         return self
#
#
#     def __next__(self):
#         x=self.n
#         self.n -= 1
#         return x
#
#
# # --- HALKAN KU TIJAABI ---
# tijaabi=Dhimis()
# it=iter(tijaabi)
# print(next(it))
# print(next(it))
# print(next(it))

#
# class SquareIt:
#     def __iter__(self):
#         self.n = 1
#         return self
#
#     def __next__(self):
#         # 1. Xisaabi square-ka nambarka hadda taagan
#         natiijada = self.n ** 2  # Ama self.n * self.n
#
#         # 2. U kordhi nambarka asalka ah si uu u diyaariyo kan xiga
#         self.n += 1
#
#         # 3. Soo celi natiijadii square-ka ahayd
#         return natiijada
#
#
# # --- TIJAABADA ---
# mishiinka = SquareIt()
# it = iter(mishiinka)
#
# print(next(it))  # 1 * 1 = 1
# print(next(it))  # 2 * 2 = 4
# print(next(it))  # 3 * 3 = 9
# print(next(it))  # 4 * 4 = 16

#
# class Istaage:
#     def __iter__(self):
#         self.n = 1
#         return self  # MAR WALBA soo celi 'self'
#
#     def __next__(self):
#         if self.n <= 5:
#             x = self.n       # Nambarka hadda taagan kaydi
#             self.n += 1
#                              # HAL KU DAR (si uu mishiinku horay u socdo)
#             return x, "waan haynaa"
#                            # Nambarkii soo celi
#         else:
#             # Markuu nambarku 5 ka weynaado, Biriigga qabo!
#             raise StopIteration
#
# # --- Tijaabada ---
# tijaabiye = Istaage()
# it = iter(tijaabiye)
#
# # Waxaad u isticmaali kartaa 'next' ama 'for loop'
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



li = [100, 200, 300]
it = iter(li)

while True:
    try:
        print(next(it))

    except StopIteration:
        print("Dhammaad: Xog kale ma jirto!")
        break








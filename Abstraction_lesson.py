# from abc import ABC, abstractmethod
#
#
# # 1. Kani waa Abstract Class-kii (Naqshaddii guud)
# # Waxaan dhaxalsiinay (ABC) si Python u ogaato inaanan laga samayn karin Object.
# class Hub(ABC):
#
#     @abstractmethod
#     def rido(self):
#         # Halkan wax code ah kuma qorayno, waayo hub kasta si gaar ah ayuu u ridaa
#         pass
#
#     def magaca_hubka(self, magac):
#         # Kan waa method caadi ah oo ay wadaagi karaan dhammaan hubka
#         print(f"Magaca hubkan waa: {magac}")
#
#
# # 2. Hadda aan samayno hub dhab ah (Subclass)
# class Bastoolad(Hub):
#     # Waa khasab inaan halkan ku qorno "rido" si barnaamijku u shaqeeyo
#     def rido(self):
#         print("Bastoolad: Boob! Boob! (Xabbad xabbad)")
#
#
# class Mashiingun(Hub):
#     # Kan isna wuxuu u ridayaa si ka duwan Bastooladda
#     def rido(self):
#         print("Mashiingun: Trrrrrrr! Trrrrrrr! (Xabbado badan)")
#
#
# # --- ISTICMAALKA ---
#
# # Ma samayn karno hub guud:
# # x = Hub()  <-- Khalad ayay ku siinaysaa (Error)
#
# # Waxaan samayn karnaa hub dhab ah:
# ba_1 = Bastoolad()
# ba_1.magaca_hubka("Glock")
# ba_1.rido()
#
# print("-" * 20)
#
# ma_1 = Mashiingun()
# ma_1.magaca_hubka("AK-47")
# ma_1.rido()

# from abc import ABC, abstractmethod
#
#
# # 1. Kani waa 'Warqaddii' ama Naqshaddii guud
# class Gaadhi(ABC):
#
#     # Abstract method: Qof kasta waa inuu qeexaa sanqadhiisa
#     @abstractmethod
#     def dhawaaq(self):
#         pass
#
#     # Abstract method: Qof kasta waa inuu sheegaa shidaalka
#     @abstractmethod
#     def shidaal(self):
#         pass
#
#     # Method caadi ah: Gaadhi kasta wuxuu leeyahay 4 lugood (waa la wadaagaa)
#     def sifo_guud(self):
#         print("Kani waa gaadhi leh 4 lugood iyo isteerin.")
#
#
# # 2. Hadda aan samayno "Baabuur Yar" (Subclass)
# class BaabuurYar(Gaadhi):
#     def dhawaaq(self):
#         print("Baabuurka Yar: Vroom! Vroom!")
#
#     def shidaal(self):
#         print("Wuxuu isticmaalaa: Baansiin.")
#
#
# # 3. Hadda aan samayno "Booyad" (Subclass kale)
# class Booyad(Gaadhi):
#     def dhawaaq(self):
#         print("Booyadda: BRRRRUUUM! (Cod weyn)")
#
#     def shidaal(self):
#         print("Wuxuu isticmaalaa: Naafto.")
#
#
# # --- ISTICMAALKA ---
#
# # Ma kaxayn karno "Naqshad" (Error ayay bixinaysaa)
# # g1 = Gaadhi()
#
# # Laakiin baabuur dhab ah waan samaysan karnaa
# my_car = BaabuurYar()
# my_car.sifo_guud()  # Tan wuxuu ka dhaxlay naqshadda guud
# my_car.dhawaaq()  # Tan isagaa iska leh
#
# print("-" * 25)
#
# big_truck = Booyad()
# big_truck.sifo_guud()
# big_truck.dhawaaq()
#
# from abc import ABC, abstractmethod
# class LacagBixin(ABC):
#         @abstractmethod
#         def dollor(self):
#             pass
#
#         @abstractmethod
#         def SHILLING(self):
#             pass
#
#
# from abc import ABC, abstractmethod  # Tani waa khasab
#
#
# # 1. Waalidka (Abstract Class)
# class LacagBixin(ABC):
#
#     @abstractmethod
#     def dollor(self):
#         pass
#
#     @abstractmethod
#     def SHILLING(self):
#         pass
#
#
# # 2. Bakhaarka (Subclass)
# class Bakhaar(LacagBixin):
#     def dollor(self):
#         print("Bakhaarku: Waad mahadsantahay maadaama aad sidatid Dollar. Soo dhowow!")
#
#     def SHILLING(self):
#         print("Bakhaarka: Maya, anigu Shillin ma rabo, sorry!")
#
#
# # 3. Shop Yar (Subclass)
# class Shop_yar(LacagBixin):
#     def dollor(self):
#         print("Shop: Maya, anigu keliya waxaan qaataa Shillin, Dollar ma rabo!")
#
#     def SHILLING(self):
#         print("Shop: Soo dhawoow maadaama aad haysatid Shillin.")
#
#
# # --- Wicitaanka (Execution) ---
#
# bakhaar = Bakhaar()
# bakhaar.dollor()
# bakhaar.SHILLING()
#
# print("-" * 20)  # Kala saare
#
# shop = Shop_yar()
# shop.dollor()
# shop.SHILLING()

from abc import ABC, abstractmethod

# Tani waa naqshadda (Waalidka la qariyay)
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Waa shaqo madhan oo la qariyay (Abstract method)

# Tani waa Class-ka dhabta ah ee hirgelinaya naqshadda
class English(Greet):
    def say_hello(self):
        print("hello")

# Tijaabo:
g = English()
# print(g.say_hello())
g.say_hello()









































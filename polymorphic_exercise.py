"""
.
Haddii hal nambar loo soo dhiibo (qiimaha shayga),
 ha soo celiyo qiimahaas isagoo lagu daray 5% canshuur ah.
Haddii laba nambar loo soo dhiibo (qiimaha iyo qiime-dhimis/discount),
qiimaha ka jar discount-ka, ka dibna ku dar 5% canshuurta.
Tilmaam: Isticmaala None si aad u maamusho labada xaaladood.
"""


class Biil:
    def xisaabi(self, qiimaha, discount=0):
        # 1. Marka hore qiimaha ka jar dhimista (haddii discount la soo dhiibo waa la jarayaa, haddii kalena waa - 0)
        qiimo_dhimis_kadib = qiimaha - discount

        # 2. Xisaabi canshuurta (5%)
        canshuur = qiimo_dhimis_kadib * 0.05

        # 3. Soo celi lacagtii oo dhan (Qiimihii dhimista kadib + Canshuurtii)
        return qiimo_dhimis_kadib + canshuur


obj = Biil()

# Xaaladda 1aad: Hal nambar (100 + 5% = 105.0)
print(f"Biilka caadiga ah: {obj.xisaabi(100)}")

# Xaaladda 2aad: Laba nambar (100 - 10 = 90, ka dibna 90 + 5% = 94.5)
print(f"Biilka leh dhimista: {obj.xisaabi(100, 10)}")


#
# Abuur Class weyn oo la yidhaahdo LacagBixin. Class-kan ha lahaado method la yidhaahdo process.
# Samee laba Class oo carruur ah: Zaad iyo EVCPlus.
# Class-ka Zaad ha soo celiyo: "Lacagta waxaa lagu bixiyay ZAAD Service."
# Class-ka EVCPlus ha soo celiyo: "Lacagta waxaa lagu bixiyay EVC Plus."
# Ugu dambayn, samee List ay ku jiraan labadaas Object,
# ka dibna isticmaal Loop si aad u daabacdo natiijada.
#
# halkan waxaan ku sameeyey class ka wayn parent class
class LacagBixin:

# Halkan ayaan ku samaynay OVERRIDING (Waxaan beddelnay shaqadii aabaha)
    def process(self):

        print("kani process kii!")

class Zaad(LacagBixin):
    def process(self):
        print("lacagta waxa lugu bixiyay zaad")

class EVCPlus(LacagBixin):
    def process(self):
        print("lacagta waxa lugu bixiyey EVCPlus")

guud=[Zaad(),EVCPlus()]
for kuritaan_variable in guud:
    kuritaan_variable.process()


class Elektaroonig:
    def description(self):
        print("kani waxa weeye elektaroonig")

class Cunto:
    def description(self):
        print("kani waxa weeye cunto")

def tusi(shay):
    # Halkan kaliya u yeer method-ka adoo isticmaalaya ()
    # Maadaama method-ku uu print leeyahay, halkan print looma baahna
    shay.description()

# Hadda si sax ah ayuu u shaqaynayaa
tusi(Cunto())        # Output: kani waxa weeye cunto
tusi(Elektaroonig()) # Output: kani waxa weeye elektaroonig




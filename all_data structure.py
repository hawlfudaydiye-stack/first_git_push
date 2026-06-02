# erey = "Kari"
#
# # Erey[0] = 'B' -> Tani qalad (TypeError) ayay ku siinaysaa.
#
# # Sida saxda ah ee loo beddelo waa in aad jarid (slicing) iyo isku-dar (+) samayso:
# erey_cusub = "B" + erey[1:]
# print(erey_cusub) # Output: Bari
#
# # Tirtirida (Deleting): Waxaad tirtiri kartaa variable-ka oo dhan adigoo isticmaalaya 'del'
# del erey_cusub
# # print(erey)# waxa soo baxaya kari sababto aah ah new string waa la saaray(del)



#
# salan = "   Waan Ku salaamay   "
#
# # 1. Dhererka (Spaces-ka waa lagu tiriyaa)
# print(len(salan)) # Output: 22
#
# # 2. Goosashada boosaska bilowga iyo dhamaadka (Strip)
# nadiif = salan.strip()
# print(nadiif)     # Output: Waan Ku salaamay
#
# # 3. Weyneyn iyo Yareyn
# print(nadiif.upper()) # Output: WAAN KU SALAAMAY
# print(nadiif.lower()) # Output: waan ku salaamay
#
# # 4. Beddelid (Replace)
# beddel = nadiif.replace("salaamay", "arkay")
# print(beddel)     # Output: Waan Ku arkay












# wadan="Somalia"
# bedel= "N" + wadan[1:]
# print(bedel)





# magaalo="soomaaliya"
# print(magaalo[::-1])



# hubiye="Palindrome"
# print("Palindrome" in hubiye )
#
#

# magaalo = "soomaaliya".lower()
# print(len(magaalo))



"""
1. Waa maxay Python List?
List waa nooc ka mid ah kaydiyayaasha xogta (Data Structures) ee Python,
 kaas oo loo isticmaalo in lagu kaydiyo xogo badan hal meel (variable).
 Liisaska Python waxay leeyihiin astaamahan muhiimka ah:

Wuu isbeddeli karaa (Mutable): Marka aad liis samayso,
dib ayaad wax uga beddeli kartaa (wax waad ku dari kartaa, waad ka tirtiri kartaa,
 waadna beddeli kartaa).
Wuu habaysan yahay (Ordered): Xogta aad geliso liiska waxay u kala horreysaa sidii aad u gelisay.
Nidaamkaas isma beddelayo ilaa adigu aad beddesho.
Wuxuu leeyahay Tix-raac (Index-based): Sida String-ga oo kale,
xog kasta waxay leedahay lambar booseed (Index) oo ka bilaabma eber (0).
Wuu isku dhex-jirnaan karaa (Heterogeneous): Hal liis wuxuu wada qaadi karaa xogo kala duwan
(tusaale: tiro, qoraal, iyo boolean).
Wuxuu oggol yahay xog soo noqnoqotay (Allows Duplicates):
Hal shay dhowr jeer ayaad liiska ku dhex qori kartaa.

"""


# Liis ka kooban tirooyin kaliya
# tirooyin = [10, 20, 30, 40]
#
# # Liis ka kooban qoraalo kaliya
# magacyo = ["Cali", "Faadumo", "Xasan"]
#
# # Liis isku dhex jira (Tiro, Qoraal, iyo Run/Been)
# isku_jir = [1, "Soomaaliya", 3.14, True]
#
# print(magacyo)
# print(tirooyin)
# print(isku_jir)


# Ka dhig qoraalka xarfo kala saaran
# xarfo = list("NABAD")
# print(xarfo) # Output: ['N', 'A', 'B', 'A', 'D']


""" list comperhension
Habkani waxa loo yaqaannaa List Comprehension. 
Waa hab aad u awood badan oo Python loogu isticmaalo si loo abuuro List cusub 
iyadoo la isticmaalayo hal layn oo koodh ah, halkii aad ka qori lahayd dhowr layn oo for loop ah.

Aynu u kala dhicidno qaybaha aad soo qortay:

Shaxda Qaabdhismeedka
[waxa_la_qabanayo for shay in meesha_laga_raadinayo if condition]
waxa_la_qabanayo (Expression): Kani waa natiijada aad rabto in lagu daro list-ga cusub. 
Waxay noqon kartaa shayga laftiisa, xisab la sameeyey, ama isbeddel lagu sameeyey xaraf (sida .upper()).
for shay in meesha_laga_raadinayo (Iteration): 
Kani waa loop-kii caadiga ahaa. Wuxuu dhex marayaa shay kasta oo ku jira List-gii hore 
ama meesha xogta laga raadinayo.
if condition (Filter): Kani waa xulasho. 
Kaliya haddii shuruudani ay True noqoto ayaa shayga lagu darayaa list-ga cusub. 
(Qaybtani waa ikhtiyaari, waad ka tegi kartaa haddii aadan shuruud rabin).
Tusaale 1: Ku dhufo 2 (Xisaab)
Aynu dhahno waxaad haysataa list lambaro ah, waxaadna rabtaa inaad abuurtu list cusub 
oo lambar kasta lagu dhuftay 2, laakiin waxaad rabtaa kuwa ka weyn 5 kaliya.


"""

#
# lambaro = [2, 4, 6, 8]
#
# # Habka List Comprehension
# cusub = [x * 10 for x in lambaro if x < 5]
#
# print(cusub)
# # Natiijadu: [12, 16]
# # Sababta: 6*2=12 iyo 8*2=16 (waayo 6 iyo 8 ayaa ka weyn 5)



# Tusaale 2: Sifaynta Magacyada (Strings)
# Aynu dhahno waxaad rabtaa inaad soo saarto magacyada ku bilaabma xarafka "A"
# oo keliya, adoo ka dhigaya xarfo waaweyn.
#

# magacyo = ["Axmed", "Cali", "Aamina", "Hani"]
#
# # Habka List Comprehension
# magacyo_a = [m.lower() for m in magacyo if len(m)>=5]
#
# print(magacyo_a)
# # Natiijadu: ['AXMED', 'AAMINA']

# cusub = [2,20,6,7,7,5]
# for x in cusub:
#     if x % 2 == 0:
#         cusub.append(x)



# cusub = [x for x in liiska if x % 2 == 0]




# numbers = [1, 2, 3, 4, 5]
# square=[x**2 for x in numbers]
# print(square)
#
# data = [10, 15, 20, 25, 30, 35]
# new_data=[x for x in data if x % 2 == 0]
# print(new_data)
#
#
# for x in data:
#    if x % 2 == 0:
#        print(x)


# magacyo = ["Cali", "Cabdi", "Hani", "Maxamed", "Leyla"]
# new_magacyo=[x for x in magacyo if len(x)<5]
# print(new_magacyo)


"""
exercise ku saabsan lis
"""

# 1. Helitaanka Index-ka (Finding Index)
# Waxaad haysataa liis magacyo ah: magaalooyin = ["Hargeisa", "Muqdisho", "Garowe", "Borama"].
# Qor koodh soo saaraya index-ka (booska) uu ku jiro magaca "Garowe"
# magaalooyin = ["Hargeisa", "Muqdisho", "Garowe", "Borama"]
# print(magaalooyin[2])

# 2. Isku-darka Liisaska (List Concatenation)
# Haddii aad haysato laba liis:
# A = [1, 2, 3]
# B = [4, 5, 6]
# Qor hal hab oo aad labadaas liis isugu darayso si aad u hesho hal liis oo ah [1, 2, 3, 4, 5, 6].
#
#
# A = [1, 2, 3]
# B = [4, 5, 6]
# A.extend(B)
# print(A)


# 3. Slicing (Goynta Liiska)
# Waxaad haysataa liiskan: xog = [10, 20, 30, 40, 50, 60, 70].
# Qor koodh soo saaraya saddexda lambar ee dhexda ku jira: [30, 40, 50]. (Isticmaal slicing).
# xog = [10, 20, 30, 40, 50, 60, 70]
# print(xog[2:5])


# 5. Jimicsi List Comprehension (Kakan)
# Waxaad haysataa liis lambaro ah: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Qor List Comprehension soo saaraya liis cusub oo:
# Lambarku hadduu yahay Chid (Even), ku dhufo 2.
# Lambarku hadduu yahay Kinsi (Odd), iska dhaafo (ha ku darin liiska cusu

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_cusu=[x*2 for x in numbers if x % 2 == 0]
# print(list_cusu)




""" TUPLES

1. Waa maxay Python Tuple?
Tuple waa ururin xogeed habaysan oo aan isbeddelin (Immutable). 
Mar haddii aad abuurto Tuple, ma dari kartid, kama saari kartid, 
waxna kama beddeli kartid xogta dhex taal.

Immutable: Lama beddeli karo abuuridda ka dib.

Ordered: Waxay u xidhan yihiin sidii aad u gelisay (Index-bay leeyihiin).

Heterogeneous: Waxay qaadi karaan xog isku dhex jirta (Tiro, qoraal, iwm).

Duplicates: Hal shay laba jeer waa ku soo noqon karaa.

2. Sida loo abuuro Tuple (Creating a Tuple)
Tuples waxaa lagu gartaa qawsaska wareegsan ().






Fiiro gaar ah: Haddii aad rabto inaad samayso Tuple leh hal shay oo kaliya, 
waa inaad raacisaa kooma , (tusaale: t = (5,)). Haddii kale, 
Python waxay u arki doontaa tiro iska dhex jirta qaws.
"""

# Tusaalooyin:
# 1. Tuple maran
# t1 = ()
#
# # 2. Tuple leh qoraal
# t2 = ('Python', 'Java', 'C++')
#
# # 3. Ka sameynta List (loo beddelay Tuple)
# liis = [1, 2, 3]
# t3 = tuple(liis)
#
# # 4. Ka sameynta String (xaraf kasta wuxuu noqonayaa xubin)
# t4 = tuple('Geeks') # Output: ('G', 'e', 'e', 'k', 's')
#
# print(t1)
# print(t2)
# print(t3)
# print(t4)

# 3. Xogta Isku-dhex-jirta (Mixed Datatypes)
# Tuple wuxuu noqon karaa "weel" weyn oo wax walba qaada,
# xitaa List ama Dictionary kale ayaa ku dhex jiri kara.
# tup_isku_jir = (10, "Hargeysa", 3.5, [1, 2], {"magac": "Axmed"})
# print(tup_isku_jir)


# 4. Helitaanka Xogta (Accessing Tuples)
# Si la mid ah List-ga iyo String-ga, waxaad isticmaalaysaa Indexing iyo Slicing.
#
# Tusaale:
#
# Python
# t = ("A", "B", "C", "D", "E")
#
# print(t[0])    # Output: A (Kowaad)
# print(t[-1])   # Output: E (Ugu dambeeya)
# print(t[1:4])


# Tuple Unpacking (Kala Furid)
# Tani waa sifo aad u qurux badan. Waxaad xogta ku dhex jirta Tuple-ka
# u qaybin kartaa variables kala duwan hal mar.
#
# Tusaale:
#
#
# khudaar = ("Tufaax", "Moos", "Canbe")
#
# # Halkan waxaan u qaybinaynaa 3 variable
# x, y, z = khudaar
#
# print(x) # Tufaax
# print(y) # Moos
# print(z) # Canbe

# 5. Isku-darka Tuples (Concatenation)
# Inkasta oo aan Tuple-ka wax laga beddeli karin, waxaad isku dari kartaa laba Tuple oo aad ka samayn kartaa mid saddexaad oo cusub adoo isticmaalaya calaamadda +.
#
# Tusaale:
#
#
# t1 = (1, 2, 3)
# t2 = ("A", "B")
# t3 = t1 + t2
# print(t3) # Output: (1, 2, 3, 'A', 'B')
"""
1. Ma aadan beddelin t1 ama t2
Markaad leedahay t3 = t1 + t2, Python dhab ahaantii ma aysan qaadan tuple-kii 
t1 si ay wax ugu dhex raddo. Taas beddelkeeda, waxay samaysay Tuple cusub 
oo gebi ahaanba ka madax bannaan kuwii hore, kaas oo la yiraahdo t3.

t1 weli waa (1, 2, 3) (sidii ay ahayd ayay u taallaa xusuusta computer-ka).

t2 weli waa ("A", "B").

t3 waa shay cusub oo dhashay.

2. Maxaa looga dhigan yahay "Waxba lagama beddeli karo"?
Macnaha Immutable (aan isbeddelin) waxa loola jeedaa in marka Tuple-ka la abuuro:

MA ku dari kartid shay cusub (sida .append() ee list-ga).

MA ka saari kartid shay (sida .remove()).

MA beddeli kartid shay ku dhex jira (tusaale t1[0] = 5 waxay ku siinaysaa Error).

Tusaale ahaan:
Haddii aad isku daydo inaad shay gudaha ah beddesho:

Python
t1 = (1, 2, 3)
t1[0] = 100  # Tani waxay keenaysaa TypeError: 'tuple' object does not support item assig

"""


# 6. Tirtiridda Tuple (Deleting a Tuple)
# Ma tirtiri kartid xubin qudha (sida del t[0]—taas waa laga mamnuucay Tuple). Laakiin waxaad tirtiri kartaa Tuple-ka oo dhan adoo isticmaalaya kelmadda del.
#
# Tusaale:
#
# Python
# t = (1, 2, 3)
# del t

# print(t) # Tani waxay ku siinaysaa Error maxaa yeelay 't' hadda ma jirto.


# 7. Kala-furidda adoo adeegsanaya Asterisk (*)
# Haddii aad leedahay Tuple dherer badan, oo aad rabto inaad qaadato
# xubinta u horraysa iyo tan u dambaysa, inta kalena aad meel ku wada raddo, waxaad isticmaali kartaa *.
#
# Tusaale:


# nambarada = (10, 20, 30, 40, 50, 60)
#
# # a = kowaad, c = ugu dambeeya, b = inta soo hadhay oo dhan
# a, *b, c = nambarada
#
# print(a) # 10
# print(b) # [20, 30, 40, 50]  <-- Waxay noqonaysaa List
# print(c) # 60



"""
Maxaa loogu baahan yahay Tuple mar haddii List jiro?
Waxaa laga yaabaa inaad is weydiiso, maxaan u isticmaali lahaa wax aan la beddeli karin?

Amniga: Haddii aad hayso xog aan la rabin in barnaamijka dhexdiisa si kedis ah looga beddelo 
(sida magacyada bilaha sanadka ama isku-duwayaasha khariidada/GPS).

Xawaaraha: Tuples-ka ayaa ka dhakhsiyo badan Lists-ka dhanka socodsiinta maadaama 
Python ogtahay inaan la beddelayn.

Dictionary Keys: Tuples-ka waxaa loo isticmaali karaa fure (key) 
ahaan Dictionary dhexdiis, laakiin List looma isticmaali karo.
"""


"""
example kaa maxaa laga wadaa bal ii sharax=Dictionary Keys: Tuples-ka waxaa loo isticmaali karaa fure (key) 
ahaan Dictionary dhexdiis, laakiin List looma isticmaali karo.

Tani waa mid ka mid ah farqiga ugu muhiimsan ee u dhexeeya Tuple iyo List. Si aad u fahanto sababta, 
waa inaan eegnaa sharciga Python u yaalla marka xog la gashanayo Dictionary.

Sharciga: "Hashable"
Dictionary-ga Python wuxuu u baahan yahay in Key-ga (furaha) uu noqdo mid aan isbeddeleyn (Immutable). 
Sababta waxay tahay Python waxay isticmaashaa hab loo yaqaan Hashing si ay xogta si degdeg ah u hesho. Haddii furaha la beddeli karo, booskii uu ku jiray ayaa lumaya.

1. Maxaa Tuple-ka loogu isticmaali karaa Key?
Maadaama Tuple-ku uu yahay Immutable (aan waxba laga beddeli karin), 
Python waxay ku kalsoon tahay in furahaas uusan isbeddelayn inta barnaamijku socdo.

Tusaale: Ka soo qaad inaad rabto inaad keydiso dhibcaha (coordinates) magaalooyinka.

Python
# Tuple loo isticmaalay Key ahaan
goobaha = {
    (9.56, 44.06): "Hargeisa",
    (2.04, 45.34): "Muqdisho"
}

print(goobaha[(9.56, 44.06)]) # Natiijadu: Hargeisa
Halkan, (9.56, 44.06) waa Tuple, waxaana loo isticmaalay Key ahaan waana sax.

2. Maxaa List-ka loogu isticmaali karin Key?
List-gu waa Mutable (waad beddeli kartaa waxa ku jira). 
Haddii Python ay kuu ogolaan lahayd inaad List ka dhigto Key, ka dibna aad List-gii wax ka beddesho, 
Dictionary-gii wuxuu noqon lahaa mid khalkhal ku jiro oo aan garanayn meel uu xogtii u raadiyo.

Tusaale (Cilad/Error):

Python
# Isku day inaad List ka dhigto Key
isku_day = {[1, 2]: "Tijaabo"} 
# Tani waxay ku siinaysaa: TypeError: unhashable type: 'list'



"""



""" 1. Waa maxay Python Dictionary?

Dictionary waa weel kaydiya xogta iyadoo u kala saaraysa Key (Fure) iyo Value (Qiimo). 
Halkii aad ka isticmaali lahayd lambar (index) si aad xog u hesho, waxaad isticmaalaysaa magac gaar ah.

Key (Fure): Waa inuu noqdaa mid gaar ah (unique) oo aan isbeddelin (sida String ama Number).

Value (Qiimo): Waa xogta furahaas ku xidhan, 
waxayna noqon kartaa wax kasta (List, Tuple, ama Dictionary kale).

Unordered/Ordered: Wixii ka dambeeyay Python 3.7, waxay u xafidantahay sidii aad u gelisay.
"""




# Tusaalooyin:


# 1. Habka caadiga ah (Fure: Qiimo)
# arday = {
#     "magac": "Jaamac",
#     "da'da": 20,
#     "magaalo": "Garowe"
# }
#
# # 2. Habka dict() function
# macalin = dict(magac="Faadumo", maadada="Xisaab")
#
# print(arday)
# print(macalin)

"""
Habka dict() waa hab ka mid ah hababka loo abuuro Dictionary-ga Python. Waxay u shaqaysaa 
sidii "Constructor" (dhise) oo kale.

Tusaalaha aad soo qortay: macalin = dict(magac="Faadumo", maadada="Xisaab") 
waa hab aad u nadiif ah oo loo qoro xogta. Aynu u kala dhicidno qaybaha uu ka kooban yahay:

1. Sida ay u shaqayso (Keyword Arguments)
Markaad isticmaalayso dict(), uma baahnid inaad isticmaasho summadda {}, 
sidoo kale uma baahnid inaad Keys-ka xigasho ("") geliso.

magac: Wuxuu noqonayaa Key-ga (Python ayaa si toos ah String uga dhigaysa).

="Faadumo": Waxa ka dambeeya summadda = wuxuu noqonayaa Value-ga.

2. Farqiga u dhexeeya dict() iyo {}
Labada habba waxay soo saarayaan natiijo isku mid ah, laakiin waxay u kala qormaan sidan:

1. Habka Caadiga ah (Dictionary Literal: {})
Kani waa habka ugu badan ee loo isticmaalo Python. Waxaad isticmaalaysaa calaamadda curly braces {}.

Keys-ka: Waa qasab inaad xigasho (quotes "") geliso haddii uu yahay String. Tusaale: "magac": "Faadumo".

Xiriiriyaha: Waxaad isticmaalaysaa summadda kolonta ah : si aad u kala saarto 
Furaha (Key) iyo Qiimaha (Value).

Qaabka: x = {"magac": "Faadumo", "da'da": 22}

2. Habka dict() Function (Constructor)
Kani waa hab loo isticmaalo function-ka dict() si xogta loogu beddelo Dictionary.

Keys-ka: Looma baahna in xigasho la geliyo markaad u dhex qorayso sida "Keyword Arguments". 
Python ayaa si toos ah String uga dhigaysa. Tusaale: magac="Faadumo".

Xiriiriyaha: Waxaad isticmaalaysaa summadda la midka ah = si aad qiimaha ugu xirto furaha.

Qaabka: x = dict(magac="Faadumo", dada=22)

Farqiga Muhiimka ah:
Xawaaraha: Habka caadiga ah {} wuu ka yara dhakhsiyo badan yahay habka dict().

Xakamaynta Keys-ka: Habka dict() kuma habboona haddii Key-gaagu uu leeyahay meel bannaan (space) 
ama uu ku bilaabmo lambar, sababtoo ah wuxuu raacayaa sharciga magacaabista variables-ka. 
Tusaale ahaan, ma dhihi kartid dict(magaalada kowaad="Hargeisa"), 
laakiin waxaad dhihi kartaa {"magaalada kowaad": "Hargeisa"}.
"""
#
# 3. Helitaanka Xogta (Accessing Items)
# Waxaad xogta ku soo saari kartaa adoo isticmaalaya Key-ga. Waxaa jira laba hab:
#
# Square Brackets []: Haddii furaha la waayo, qalad (Error) ayuu ku siinayaa.
#
# .get() Method: Haddii furaha la waayo,
# wuxuu kuu soo celinayaa None (kuma siinayo Error), taas oo ka dhigaysa hab ammaan ah.
#
# Tusaale:
#
#
# gaadhi = {"nooc": "Toyota", "sanad": 2022}
#
# # Habka 1aad
# print(gaadhi["nooc"]) # Output: Toyota
#
# # Habka 2aad (Safe way)
# print(gaadhi.get("midab")) # Output: None (sababtoo ah "midab" kuma jiro)
# 4. Ku-darista iyo Beddelista (Adding and Updating)
# Maadaama Dictionary-gu uu yahay Mutable, waad beddeli kartaa xogtiisa ama xog cusub ayaad ku dari kartaa
# adoo isticmaalaya isla habka xogta loo helo.
#
# Tusaale:
#
#
# buug = {"cinwaan": "Halgankii Nolosha", "bogga": 150}
#
# # Beddel xog hore (Update)
# buug["bogga"] = 200
#
# # Ku dar xog cusub (Add)
# buug["qoraa"] = "Maxamed Cali"
#
# print(buug)
# # Output: {'cinwaan': 'Halgankii Nolosha', 'bogga': 200, 'qoraa': 'Maxamed Cali'}

# 5. Ka-saarista Xogta (Removing Items)
# Waxaa jira dhowr waddo oo wax looga tirtiro:
#
# pop(key): Wuxuu tirtiraa furaha aad siisay, wuxuuna kuu soo celinayaa qiimihiisii.
#
# popitem(): Wuxuu tirtiraa kii ugu dambeeyay ee la geliyay.
#
# del: Wuxuu tirtiraa fure gaar ah ama dictionary-ga oo dhan.
#
# clear(): Wuxuu ka dhigayaa mid maran {}


# 0. Bilowga: Dictionary leh 4 xogood
arday = {
    "magac": "Abdilahi",
    "da'da": 23,
    "magaalo": "Hargeisa",
    "aqoon": "AI Developer"
}

# # 1. pop(key): Tirtir "da'da", laakiin qiimihii gacanta ku hay
# da_hore = arday.pop("da'da")
# print(f"Waxaa la tirtiray da'dii oo ahayd: {da_hore}")
# # Natiijada: {'magac': 'Abdilahi', 'magaalo': 'Hargeisa', 'aqoon': 'AI Developer'}
#
# # 2. popitem(): Tirtir kii ugu dambeeyay ee la geliyay (aqoon)
# shayga_u_dambeeyay = arday.popitem()
# print(f"Waxaa la saaray kii u dambeeyay: {shayga_u_dambeeyay}")
# # Natiijada: {'magac': 'Abdilahi', 'magaalo': 'Hargeisa'}
#
# # 3. del: Tirtir "magaalo" si toos ah (waxba dib kuuma siinayo)
# del arday["magaalo"]
# # Natiijada: {'magac': 'Abdilahi'}
#
# # 4. clear(): Ka dhig maran (empty) Dictionary-ga oo dhan
# arday.clear()
# print(f"Natiijada ugu dambeysa: {arday}")
# # Natiijada: {}


"""
maxaa lagawadaa wuxuu soo celinayaa xogtiisa bal halkaa ii sahrax=pop(key): 
Wuxuu tirtiraa furaha aad siisay, wuxuuna kuu soo celinayaa qiimihiisii.

Tani waa mid ka mid ah sifooyinka ugu muhiimsan ee .pop(), 
waana waxa uu kaga duwan yahay amarka del. Marka la leeyahay 
"Wuxuu soo celinayaa xogtiisa" (returns the value), 
waxaa loola jeedaa in Python aysan kaliya tirtirin shayga, 
balse ay gacanta kuugu soo qabanayso qiimihii (value) uu lahaa shaygaas ka hor intaan la tuurin.

Si kale haddii loo dhigo: pop() wuxuu u shaqeeyaa sidii adoo qof wax ka dafay; 
shaygii booskaas waa ka baxayaa, laakiin adiga ayaa gacanta ku haya oo isticmaali kara.

Tusaale Toos Ah:
Ka soo qaad inaad haysato Dictionary xogta ardayga ah, oo aad rabto inaad ka saarto 
magaalada uu deggan yahay, laakiin aad rabto inaad magaaladaas meel kale ku isticmaasho.

Python
arday = {
    "magac": "Abdilahi",
    "magaalo": "Hargeisa",
    "maaddo": "Python"
}

# Halkan waxaan isticmaalaynaa .pop()
# Waxaan tirtiraynaa "magaalo", qiimiheedana waxaan ku kaydinaynaa "m_cusub"
m_cusub = arday.pop("magaalo")

print(arday)      # Natiijadu: {'magac': 'Abdilahi', 'maaddo': 'Python'} (Magaaladii waa ka baxday)
print(m_cusub)    # Natiijadu: Hargeisa (Qiimihii ay lahayd gacantaad ku haysaa!)
Maxay muhiim u tahay inuu xogta soo celiyo?
Waxaa jira xaalado badan oo aad u baahan tahay inaad shayga ka saarto hal meel, 
laakiin aad meel kale u wareejiso.

Tusaale: Haddii aad haysato liiska dadka online-ka ah, markuu qofku baxo (logout), 
waxaad isticmaalaysaa .pop() si aad magaciisa uga saarto liiska dadka hadda jooga, 
isla markaana aad magacaas ugu darto liiska dadka "Offline-ka" ah.

Farqiga u dhexeeya pop() iyo del:
pop(key): Wuxuu tirtiraa shayga, laakihiin wuxuu kuu dhiibayaa qiimihii uu lahaa (Value). 
Haddii aad isku daydo inaad tirtirto Key aan jirin, waad u sheegi kartaa waxa uu soo celinayo si uusan 
"Error" u bixin (tusaale: arday.pop("da'da", "Lama helin")).

del arday["key"]: Isagu wuu tirtiraa shayga kaliya, waxba dib kuuma siiyo. 
Haddii Key-gu jirinna, koodhku wuxuu ku siinayaa "Error" toos ah.

"""

# 6. Dul-maridda Dictionary-ga (Iteration)
# Waxaad isticmaali kartaa for loop si aad u aragto furayaasha, qiimayaasha, ama labadaba.
#
# Tusaale:


# shirkad = {"magac": "Telesom", "goobta": "Hargeysa"}

# 1. Furayaasha kaliya (Keys)
# for x in shirkad:
#     print(x)

# 2. Qiimayaasha kaliya (Values)
# for y in shirkad.values():
#     print(y)

# # 3. Labadaba (Key and Value)
# for k, v in shirkad.items():
#     print(f"Furaha waa {k}, Qiimuhuna waa {v}")


# 7. Dictionary dhexdiis Dictionary kale (Nested Dictionaries)
# Tani waxay kuu ogolaanaysaa inaad xog aad u adag habayso. Tusaale ahaan, hal liis oo qoys ah oo qof kasta dictionary u gaar ah leeyahay.
#
# Tusaale:

#
# qoyska = {
#     "ilmo1": {"magac": "Hinda", "sano": 5},
#     "ilmo2": {"magac": "Cumar", "sano": 10}
# }
#
# # Sida loo helo magaca ilmo2
# print(qoyska["ilmo2"]["magac"]) # Output: Cumar
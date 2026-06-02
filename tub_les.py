# exercise
#
#
# Unpacking: Abuur tuple la yiraahdo person oo leh magacaaga iyo da('daada.'
# ' Ka dib, labadaas xogood ku kala rido laba doorsoome (variables) oo kala ah name iyo age, markaas ka dib daabac name.)

# person=("abilahi", 21)
# name,age=person
# print(name)


# Checking: Qor koodh hubinaya in magaca "Python" uu ku jiro tuple-ka soo socda:
# langs = ("Java", "C++", "Python", "Ruby"). Haddii uu ku jiro, ha soo daabaco "Wuu ku jiraa".

# langs = ("Java", "C++", "Python", "Ruby")
#
# # Hubinta isticmaalka 'in'
# if "Python" in langs:
#     print("Wuu ku jiraa")



# # 1. Qeexidda Tuple-ka
# numbers = (1, 2, 3, 2, 4, 2, 5)
#
# # 2. Isticmaalka .count() si loo helo inta jeer ee 2 soo laabtay
# inta_jeer = numbers.count(2)
#
# # 3. Daabacaadda natiijada
# print(inta_jeer)

# Nested Tuples (Tuple dhex fadhiya Tuple kale):
# Waxaad haysataa Tuple: data = ("Hargeisa", (2025, 2026), "Somalia").
# Qor koodh soo saaraya sanadka 2026 oo kaliya. (Haddii aad u baahato caawimaad: isticmaal laba index oo isku xiga sida data[1][1]).





# data = ("Hargeisa", (2025, 2026), "Somalia")
# print(data[1][1])




# Tuple to String:
# Waxaad haysataa Tuple magacyo ah: magacyo = ('A', 'B', 'D', 'I').
# Maadaama aad ogtahay in Tuple-ka xogtiisa la akhrisan karo, isku day inaad Loop (for loop)
# u isticmaasho si aad u daabacdo xaraf kasta isaga oo goonni u taagan.

# magacyo = ('A', 'B', 'D', 'I')
# for i in magacyo():
#     char=+i;
#     print(i)


#
# Waxaad haysataa tuple: my_tuple = (10, 20, 30, 40, 50).
# Qor koodh soo saaraya tuple-ka isagoo foorara (gadaal ka soo bilaabmaya): (50, 40, 30, 20, 10).


# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[::-1])

#
# 2. Finding the Index (Raadinta Booska)
# Waxaad haysataa tuple magacyo ah: ardayda = ("Ahmed", "Jama", "Muna", "Leyla").
# Qor koodh kuu sheegaya Index-ka (booska) uu ku jiro magaca "Muna"

# ardayda = ("Ahmed", "Jama", "Muna", "Leyla")
# print(ardayda[2])


#
# Summing Numbers (Isku darka)
# Waxaad haysataa tuple lambaro ah: scores = (85, 90, 75, 100).
# Qor koodh isku daraya dhammaan dhibcahaas (Sum) ka dibna soo daabacaya wadarta guud.

# scores = (85, 90, 75, 100)
# wadarta= (sum(scores))
# print(wadarta)



# 4. Nested Tuple Access (Gudaha u gal)
# Waxaad haysataa tuple qasan: nested = (1, 2, ("Python", "Java"), 3).
# Qor koodh soo saaraya oo kaliya erayga "Python".



# nested = (1, 2, ("Python", "Java"), 3)
# print(nested[2][0])




#
# 5. Tuple Expansion (Kordhinta)
# Waxaad haysataa tuple: t1 = (1, 2, 3).
# Waxaad rabaa inaad ku darto lambarka 4,
# laakiin maadaama aan la beddeli karin, isticmaal habka Concatenation (+) si aad u abuurto tuple cusub oo ah (1, 2, 3, 4).

t1 = (1, 2, 3)
t2=  (4,)


print(t1+t2)

















# 1. Jimicsiga 1-aad: Labanlaabka (Map)
# Haysato liis nambarada ah: nambarada = [1, 2, 3, 4, 5].
#
# Shaqadaada:
# Isticmaal map() iyo lambda si aad u soo saarto liis cusub oo nambar kastaa uu yahay square (tusaale: 2→4, 3→9).

# labolaab = [1, 2, 3, 4, 5]
#
# natiijo = list(map(lambda x: x**2, labolaab))
#
# print(natiijo)

# 2. Jimicsiga 2-aad: Shaandhaynta (Filter)
# Haysato liis da'da dadka ah: da'da = [12, 18, 25, 15, 30, 8, 40].
#
# Shaqadaada: Isticmaal filter() iyo lambda si aad u soo saarto dadka ka weyn 18 sano oo qura.

# da_da = [12, 18, 25, 15, 30, 8, 40]
# soosaar= list(filter(lambda x: x>=18,da_da))
# print(soosaar)


# 3. Jimicsiga 3-aad: Habaynta Magacyada (Sorted)
# Haysato liis magacyo ah oo kala yaal: magaalooyin = ["Muqdisho", "Boosaaso", "Hargeisa", "Garowe"].
#
# Shaqadaada: Isticmaal sorted() iyo lambda si aad u habayso magacyada adoo eegaya xarafka ugu dambeeya magac kasta



# 5. Jimicsiga 5-aad: Xarfaha Waaweyn (Lambda + Filter)
# Haysato liis erayo ah: erayo = ["python", "is", "awesome", "ai"].
#
# Shaqadaada: Isticmaal filter() si aad u soo saarto erayada dhererkoodu ka weyn yahay 3 xaraf.


# Lambda qaadanaysa 'x' kuna dhuphanaysa 10
# toban_laab = lambda x : x * 10

# print(toban_laab(5))   # Natiijada: 50
# print(toban_laab(12))  # Natiijada: 120



xog = ["Arday1", "12345", "Macalin", "Arday2", "!!"]

# 1. Soo saar kaliya kuwa xarfaha ah (.isalpha)
xarfo_kaliya = list(filter(lambda x: x.isalpha(), xog))

# 2. Soo saar kuwa ku bilaabma "Arday" (.startswith)
ardayda = list(filter(lambda x: x.startswith("Arday"), xog))

# 3. Soo saar kuwa nambarada ah (.isdigit)
nambaro = list(filter(lambda x: x.isdigit(), xog))

ku_dhamaada=list(filter(lambda x: x.endswith("n"),xog))

print(f"Xarfo: {xarfo_kaliya}")
print(f"Ardayda: {ardayda}")
print(f"Nambaro: {nambaro}")
print(f"xarfo_yar-yar:{ku_dhamaada}")












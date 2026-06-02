# Haddii la ku siiyo variable-ka ah



# magac = "Hargeisa"
#
# print(magac[0])
#
# print(magac[-1])

#
# Waxaad haysataa variable-ka
# Sidee ayaad ku heli kartaa oo kaliya kelmadda "Python" adiga oo isticmaalaya slicing?

# kelmad = "Barashada Python"
# print(kelmad[9:])


# tirooyin = "0123456789"
# print(tirooyin[1:8:2])



# Sidee ayaad hal xariiq oo kood ah ugu gaddooni kartaa
# (reverse) string-ka
#
#
# fariin = "Hello" si uu u noqdo "olleH"
# fariin = "Hello"
# print(fariin[::-1])

# Isku dhaf (Challenge)
# Waxaa jira variable ah data = "2026-Project-AI".
#
# Qor koodka soo saaraya sanadka oo kaliya (2026).
#
# Qor koodka soo saaraya ereyga ugu dambeeya (AI) adigoo isticmaalaya negative indexing.




# data = "2026-Project-AI"
#
# print(data[0:4])
# print(data[-2::])



# String Iteration waa habka mid-mid loogu dul maro xarfaha ama calaamadaha ka kooban qoraal (String).
# s = "somalia"
# for char in s:
#   print(char)

# s = "Python"
# for char in s:
#  print(char)


'''
Deleting a String
It's not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.

'''
# s="qorsheeye"
# del s



# 1. len()
# Wuxuu xisaabiyaa wadarta guud ee xarfaha, calaamadaha, iyo xitaa meelaha banaan (spaces).
#
# magac = "Somali Python"
# dherer = len(magac)
#
# print(f"Dhererka qoraalku waa: {dherer}")
# # Natiijadu waa 13 (maxaa yeelay space-ka dhexda ku jira waa la tirinayaa)




# upper() iyo lower()
# Waxay u beddelaan qoraalka far-waawayn ama far-yaryar.
#
#
# oraah = "Barashada Python waa Fududahay"
#
# print(oraah.upper()) # Natiijada: BARASHADA PYTHON WAA FUDUDAHAY
# print(oraah.lower()) # Natiijada: barashada python waa fududahay
#


# 3. strip()
# Wuxuu nadiifiyaa meelaha banaan (extra spaces) ee ku yaalla bilowga iyo dhamaadka qoraalka, laakiin ma taabto kuwa dhexda ku jira.
#
#
# qoraal = "    Hel    lo World    "
# nadiif = qoraal.strip()
#
# print(f"markuu hore:'{qoraal}'") # Sida uu ahaa (leh space)
# print(f"marka after:'{nadiif}'") # Isagoo nadiif ah (Natiijada: 'Hello World')
#
#

# 4. replace()
# Wuxuu raadiyaa eray ama xaraf gaar ah, ka dibna wuxuu ku beddelaa mid kale.


# text = "Waxaan jecelahay Java"
# cusub = text.replace("Java", "Python")
#
# print(cusub) # Natiijada: Waxaan jecelahay Python
#
#
#
# Tusaale Isku-dhafan (Laba shaqo oo isku mar ah)
# Python dhexdeeda, waxaad isku xiri kartaa dhowr shaqo hal mar (tan waxaa la dhahaa Method Chaining):
#
# Python
# xog = "   shirka python   "
# # Waxaan rabnaa inaan space-ka ka saarno, hadana ka dhigno far-waawayn
# natiijo = xog.strip().upper()
#
# print(f"Natiijada: '{natiijo}'")
# # Natiijada: 'SHIRKA PYTHON'



s="geeksforgeeks"
del s
# print(s[1:-6])







































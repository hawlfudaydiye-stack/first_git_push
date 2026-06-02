# # 1. Tirada iyo Labanlaabkeeda
# # Abuur liis ka kooban labanlaabka tirooyinka u dhaxeeya 1 ilaa 10 (10-ku ha ku jiro).
#
# Input: range(1, 11)
#
# Natiijada la rabo: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# labo_laanb=[x*2 for x in range(1,11)]
# print(labo_laanb)
#
# 2. Dhererka Erayada (String Length)
# Waxa aad haysataa liis magacyo ah: magaalooyin = ["Hargeisa", "Muqdisho", "Borama", "Garowe"].
# Abuur liis cusub oo sheegaya dhererka (length) magac kasta inta xaraf uu ka kooban yahay.
#
# Natiijada la rabo: [8, 8, 6, 6]

# dhererka=["Hargeisa", "Muqdisho", "Borama", "Garowe"]
#
# dherer=([len(x) for x in dhererka])
# print(dherer)
# 3. Shaandheynta Xarfaha (Filtering Strings)
# Waxa aad haysataa liis ereyo ah: qalab = ["Laptop", "Mouse", "Keyboard", "Monitor", "Mic"].
# Abuur liis cusub oo ay ku jiraan oo kaliya ereyada ka bilaabma xarafka "M".
#
# # Natiijada la rabo: ['Mouse', 'Monitor', 'Mic']
#
# qalab = ["Laptop", "Mouse", "Keyboard", "Monitor", "Mic"]
# hubiye=[x for x in str ]
#
#
# Inaad Loop ku dhex marto (Iterating)
# Marka hore, waa inaad mid-mid u soo qabataa magacyada
# ku jira liiska qalab. Tani waxay kuu ogolaanaysaa inaad magac kasta goonidiisa u baarto.
#
#
#
#
#

# magaalo = ["Hargeisa", "Muqdisho", "Garowe"]
# for m in magaalo:
#     print(m)

#
# matrix = [[1, 2], [3, 4]]
# print(matrix[1][1]) # Waxay soo saaraysaa 2 (Safka 1aad, Booska 2aad)




# khudaar=["moos","tufaaax"]
#
#
# khudaar.pop(0)
#
# print(khudaar)


# nums = [10, 20, 30]
# nums.pop()
# print(nums)



# dhaw=[x-2 for x in range(1,11)]
# print(dhaw)


# Halkii aad dhihi lahayd arday = ["Axmed", 21] (ma garanaysid 21 waxay tahay)
arday = {"magac": "Axmed", "da'da": 21}

print(arday["magac"])  # Natiijada: Axmed
print(arday["da'da"])
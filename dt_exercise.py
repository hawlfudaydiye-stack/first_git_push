# 1. Layliga Indexing-ka
# Waxaa lagu siiyay string-kan: s = "SomaliGeeks".
#
# Soo saar xarafka u horreeya (S).
#
# Soo saar xarafka u dambeeya adiga oo isticmaalaya Negative Indexing.

# s = "SomaliGeeks"
# print(s[-1])


# 2. Layliga Slicing-ka
# Isla string-kaas s = "SomaliGeeks":
#
# Ka goo qaybta ah "Geeks".
#
# Qoraalka oo dhan u rog lixdami (Reverse) adiga oo isticmaalaya slicing.

# s = "SomaliGeeks"
# print(s[6:])
# print(s[::-1])


#
# 3. Layliga Beddelka (Replace)
# Waxaa jira weedh ah: text = "Barashada Python waa adag tahay".
#
# Isticmaal habka (method) ku habboon si aad ereyga "adag" ugu beddesho "fudud".

# text = "Barashada Python waa adag tahay"
# bedel=text.replace("adag","fuduud")
# print(bedel)




# 4. Layliga F-Strings
# Abuur labo variable: magac = "Axmed" iyo da' = 25.
#
# Isticmaal f-string si aad u daabacdo: "Magacaygu waa Axmed, waxaana jiraa 25 sano."
#
# magac = "Axmed"
# da = " 25"
# print(f"magacayg waa {magac}{da}")



# 5. Layliga Hubinta (Membership)
# Hubi in ereyga "Python" uu ku dhex jiro string-kan: "Barashada Python waa mid xiiso leh".
# (Waa in natiijadu kuu soo baxdaa True).



# text = "Barashada java waa mid xiiso leh"
#
# # Halkan waxaan ku leenahay: "Python" ma ku jiraa text?
# natiijo = "Python" in text
#
# print(natiijo)
# # Output: True


# check="hooyo macaan iska waran      "
# hubiye="hooyo"in check
# print(hubiye)



# sifeeye

check="  asc       hooyo macaan iska waran            "
hubiye = check.strip()
print(hubiye)








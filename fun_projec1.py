# def xisaabi_adeega(magace,qiimaha_asalka,cashuurta=5):
#
#     lacagta_cashuurta=qiimaha_asalka*cashuurta/100
#
#     wadarta_guud = qiimaha_asalka+lacagta_cashuurta
#
#     return f"magaca adeega:{magace} | qiimaha:{qiimaha_asalka} | cashuurta:{lacagta_cashuurta} | wadarta:{wadarta_guud}"
#
# dhamaan=xisaabi_adeega("internet",50)
# print(dhamaan)
#
# xisaabiye2=xisaabi_adeega("cup caffee",2)
# print(xisaabiye2)
#
#
#
# def xisaabi_darajo(magac,dhibcaha):
#
#
#
#
#     if dhibcaha>=90:
#         Darajo='A'
#     elif dhibcaha>=80:
#         Darajo='B'
#     else:
#         Darajo='C'
#
#     return f"ardayga:{magac}|darajadiisu waa:{Darajo}"
#
# guud_ahaan=xisaabi_darajo("abdiaahi jama",90)
# print(guud_ahaan)
#
# guud_ahaan1=xisaabi_darajo("safa jama",86)
# print(guud_ahaan1)
#
# guud_ahaan2=xisaabi_darajo("mohamed jama",40)
# print(guud_ahaan2)
#



# waa function ls isticmsslsyo *ags
# def xisaabi_celceliska(magac, *dhibcaha):
#     # 1. Xisaabi celceliska (Average)
#     # Talo: wadarta u qaybi inta ay le'eg yihiin dhibcuhu
#     wadarta= sum(dhibcaha)
#     celcelis = sum(dhibcaha) / len(dhibcaha)
#
#
#     # 2. Hadda isticmaal 'if' iyo 'elif' si aad darajo u siiso celceliskaas
#     if celcelis >= 90:
#         darajo = "A"
#     elif celcelis >= 80:
#         darajo = "B"
#     else:
#         darajo = "C"
#
#
#
#     return f"Ardayga: {magac} | Celceliska: {celcelis} | Darajada: {darajo}"
#
#
# # --- HALKAN KU TIJAABI ---
# # Ardaygan wuxuu keenay 3 maaddo: 80, 90, 100
# print(xisaabi_celceliska("Abdiaahi", 80, 90, 100))
#
# # Ardaygan wuxuu keenay 2 maaddo oo kaliya: 70, 75
# print(xisaabi_celceliska("Safa", 70, 75))











def xisaabi_celceliska(magac, *dhibcaha, **macluumaad):
    # 1. Xisaabi celceliska
    celcelis = sum(dhibcaha) / len(dhibcaha)

    # 2. Darajada go'aami
    if celcelis >= 90:
        darajo = "A"
    elif celcelis >= 80:
        darajo = "B"
    else:
        darajo = "C"

    # 3. Diyaarinta tafaasiisha **macluumaad (kwargs)
    # Waxaan u beddelaynaa qoraal hal xariiq ah si loogu daro return-ka
    tafaasiil = ""
    for fure, qiime in macluumaad.items():
        tafaasiil += f" | {fure}: {qiime}"

    # 4. Soo celi natiijada oo dhan oo isku xiran
    return f"Ardayga: {magac} | Celceliska: {celcelis:.1f} | Darajada: {darajo}{tafaasiil}"


# --- HALKAN KU TIJAABI ---

# Ardayga 1aad: Waxaan u raacinay Da'da iyo Magaalada
print(xisaabi_celceliska("Abdiaahi", 80, 90, 100, Da_da=22, Magaalada="Hargeisa"))

# Ardayga 2aad: Waxaan u raacinay Dugsiga kaliya
print(xisaabi_celceliska("Safa", 70, 75, Dugsiga="Iftin"))

# Ardayga 3aad: Ma laha wax tafaasiil dheeraad ah
print(xisaabi_celceliska("Maxamed", 85, 95))
# Mashruuca: Hubinta Martida (No Duplicates)
guests = set()
# saxa ay ku siinaysaa set madhan oo aad wax ku soo kurto



# guests = set(["Faarax"])

'''
Talo: Hadii aad rabto inaad barnaamijkaaga ku bilowdo adigoo magaca "Faarax" horey ugu daray,
 isticmaal qawsaska jactadda ah:
guests = {"Faarax"} ama guests = set(["Faarax"]).

Laakiin haddii aad rabto inaad martida hadhow hal-hal ugu darto adoo isticmaalaya input(),
 qaabka ugu habboon waa kii aad hore u isticmaashay ee ahaa: guests = set().

'''



# guests = set()
'''
Hadii aad u qorto guests = set('faarax'), Python waxay u dhaqmi doontaa si ka duwan sidii aad filaysay. Halkii ay hal magac oo "Faarax" ah kaydin lahayd, waxay u kala jabinaysaa xarfo (characters).

Waa kuwan saddexda shay ee dhacaya:

1. Wuxuu u kala qaadayaa Xarfo (String Iteration)
Function-ka set() marka la siiyo hal "string", wuxuu ula dhaqmaa sidii liis xarfo ah.
 Sidaas darteed, wuxuu qaadayaa xaraf kasta oo ku jira 'faarax'.

2. Wuxuu tirtirayaa Xarfaha isku midka ah (Removing Duplicates)
Maadaama uu yahay Set, ma oggolaanayo wax soo laablaabma. Magaca 'faarax' waxaa ku jira labo 'a'.
 Set-ku wuxuu reebayaa hal 'a' oo qura.

3. Ma jiro nidaam u go'an (Unordered)
Set-ku ma dhowro nidaamka xarfaha. Natiijadu ma ahaan doonto 'f', 'a', 'a', 'r', 'a', 'x',
 ee waxay noqon doontaa isku dhex yaas.

Natiijada rasmiga ah (Output):
Hadii aad print(guests) dhahdo, waxaad arki doontaa wax u dhow kan:
{'f', 'a', 'r', 'x'}

'''
# guests = set(["abdilahi", "ahmed", "faarax"])
# guests2 = set(["hinda", "shadow", "faarax"])
#
#
# def invite_guest(name):
#     name = name.lower()
#     # Hubi haddii uu ku jiro liiska koowaad ama kan labaad
#     if name in guests or name in guests2:
#         print(f"Digniin: {name} mar hore ayaa la casuumay!")
#     else:
#         # Halkan waxaad go'aansan kartaa liiska aad ku darayso
#         guests.add(name)
#         print(f"Casuumad: {name} waa lagu daray.")
#
#
# def remove_guest(name):
#     name = name.lower()
#     found = False
#
#     if name in guests:
#         guests.remove(name)
#         found = True
#     if name in guests2:
#         guests2.remove(name)
#         found = True
#
#     if found:
#         print(f"{name} waa laga saaray.")
#     else:
#         print(f"Khalad: {name} lama helin.")
#
#
# # Tijaabo
# remove_guest("faarax")  # Wuxuu ka saarayaa labadaba
# print(f"Liiska 1: {guests}")
# print(f"Liiska 2: {guests2}")

# 1. Kaydka Dukaanka
products = {"Saacad": 20, "Kabaha": 45, " Shaadh": 15}
cart = []

print("Ku soo dhawaada dukaanka! Alaabta na taal waa:")
for item, price in products.items():
    print(f"- {item}: ${price}")

# 2. User Input Loop
while True:
    choice = input("\nQor magaca alaabta aad rabto (ama qor 'exit' si aad u bixiso lacagta): ").capitalize().strip()

    if choice == "Exit":
        break

    # Halkan ku dar Logic-ga lagu hubinayo haddii 'choice' uu ku jiro 'products'
    # Haddii uu jiro, ku dar 'cart'. Haddii kale, u sheeg inaan la hayn.

# 3. Xisaabinta Wadarta (Total)
total_price = 0
print("\n--- Alaabta aad iibsatay ---")
# Halkan isticmaal 'for loop' aad ku dhex marayso List-ka 'cart'
# Si aad u hesho qiimaha shay kasta, isticmaal: products[shayga]













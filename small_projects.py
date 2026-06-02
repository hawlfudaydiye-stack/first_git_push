# # 1. Dictionary-ga bilowga ah
# contacts = {"Abdilahi": "063123456", "Sacaad": "063987654"}
# while True:
#  print("--- MAAMULKA TELEFANNADA ---")
#  print("1. Ku dar xog cusub")
#  print("2. Raadi qof")
#  print("3. Muuji dhammaan")
#  print("4. xog ka saar")
#
#  user_choice = input("Dooro lambar (1/2/3/4): ")
#
# # 1. Qaybta lagu darayo (Isticmaal "1" oo qoraal ah)
#  if user_choice == "1":
#     print("\n--- Ku dar xogta ---")
#     magac = input("Gali magaca qofka: ")
#     telefan = input("Gali lambarkiisa: ")
#
#     contacts[magac] = telefan
#     print(f"Si guul leh ayaa loo kaydiyey {magac}!")
#
# # 2. Qaybta Raadinta
#  elif user_choice == "2":
#     print("\n--- Raadi qof ---")
#     magac = input("Gali magaca aad raadinaysid: ")
#
#     if magac in contacts:
#         # Halkan waxaan ka soo saaraynaa lambarka (Value-ga)
#         print(f"Haa, waa la helay! Lambarka {magac} waa: {contacts[magac]}")
#     else:
#         print("Waan ka xunnahay, magacaas kuma jiro diiwaanka.")
#
# # 3. Qaybta Muujinta guud
#  elif user_choice == "3":
#     print("\nDhammaan xogta hadda jirta:", contacts)
#
#  elif user_choice == "4":
#      print("\n--- Tirtir xog ---")
#      magac = input("Gali magaca qofka aad rabto inaad tirtirto: ")
#
#      if magac in contacts:
#          # Habka .pop() wuxuu tirtiraa fureha, wuxuuna soo celiyaa qiimihiisa
#          lambar = contacts.pop(magac)
#          print(f"Si guul leh ayaa loo tirtiray {magac} oo lambarkiisu ahaa {lambar}.")
#      else:
#          print("Magacaas lama tirtiri karo waayo kuma jiro diiwaanka.")
#
#
#  else:
#     print("Dooro mid ka mid ah 1, 2, ama 3  iyo 4 oo keliya.")
#
#  masii_wadaysaa = input("ma sii wadaysaa: (y/n)")
#  if masii_wadaysaa == 'n':
#   break

# 1. Kaydka xogta (Global Dictionary)
inventory = {"Laptop": 3, "Mouse": 50, "Keyboard": 20}


# 2. Functions-ka (Ficilada)

def display_inventory():
    """Wuxuu soo bandhigaa dhamaan agabka bakhaarka ku jira"""
    print("\n--- LIISKA AGABKA ---")
    if not inventory:
        print("Bakhaarku waa madhan yahay!")
    else:
        for item, quantity in inventory.items():
            print(f"Agabka: {item:<5} | Tirada: {quantity}")


def add_item(magac, quantity):
    """Wuxuu ku daraa agab cusub ama wuxuu ku kordhiyaa mid hore u jiray"""
    if magac in inventory:
        inventory[magac] += int(quantity)  # Haddii uu jiray, ku dar tirada cusub
    else:
        inventory[magac] = int(quantity)  # Haddii kale, abuuri key cusub
    print(f"\nGuul: Waxaa la cusboonaysiiyay {magac}.")


def update_quantity(magac, cusboonaysiin):
    """Wuxuu gabi ahaanba beddelaa tirada shay hore u jiray"""
    if magac in inventory:
        inventory[magac] = int(cusboonaysiin)
        print(f"\nGuul: {magac} tiradiisii waxaa laga dhigay {cusboonaysiin}.")
    else:
        print(f"\nKhalad: '{magac}' kuma jiro bakhaarka, markaa lama beddeli karo.")


def search_item(magac):
    """Wuxuu baadhaa in shay ku jiro bakhaarka iyo in kale"""
    if magac in inventory:
        print(f"\nNatiijo: Haa, '{magac}' waa la hayaa. Waxaa yaalla {inventory[magac]} xabbo.")
    else:
        print(f"\nNatiijo: Maya, '{magac}' kuma jiro liiska bakhaarka.")


def delete_item(magac):
    if magac in inventory:
        del inventory[magac]


        print(f"waan ka saarnay, '{magac} '")
    else:
        print(f"waan ka xunnahay lama hayo, '{magac}'")


def total_stock():
    # 1. Waxaan soo qabanaynaa dhammaan tirada (values) annagoo isticmaalayna list comprehension
    # 2. Ka dibna waxaan isugu geynaa sum()
    wadarta = sum([tirada for tirada in inventory.values()])


   # qaabka ugu gaaban aduunka
   #  sum(inventory.values())
    # hadaan isticmaali lahaa for loop sidan ayuu u ee kaan lahaa
    # wadarta = 0
    # for tirada in inventory.values():
    #     wadarta = wadarta + tirada

    print(f"\nWadarta guud ee dhammaan alaabta bakhaarka taal waa: {wadarta} xabbo.")


def low_stock_check():
    # 1. Waxaan soo qabanaynaa values-ka uun
    # 2. Waxaan dhihibaynaa lambda x: x < 5 (oo ah: x ka yar 5)
    # 3. Waxaan u beddelaynaa list si aan u print-gareeyno
    natiijo = list(filter(lambda x: x <= 5, inventory.values()))

    if natiijo:
        print(f"Digniin: Waxaa jira alaab ka yar 5 xabbo: {natiijo}")
    else:
        print("Dhammaan alaabta bakhaarku way ku filan tahay (dhamaantood waa 5+).")
# 3. Main Loop (Menu-ga barnaamijka maamulaya)

while True:
    print("\n==============================")
    print("   MAAMULKA BAKHAARKA (V1.0)")
    print("==============================")
    print("1. Fiiri Agabka (Display)")
    print("2. Ku dar Agab Cusub (Add)")
    print("3. Beddel Tirada (Update)")
    print("4. Baadh Agab (Search)")
    print("5.delete:)")
    print("6. xisaabi wadarta guud")
    print("7. dhamaan raba")
    print("8. Ka Bax (Exit)")




    choice = input("Dooro ficilka aad rabto (1-7): ")

    if choice == "1":
        display_inventory()

    elif choice == "2":
        m = input("Enter magaca alaabta: ")
        q = input("Geli tirada: ")
        add_item(m, q)

    elif choice == "3":
        m = input("Enter magaca alaabta aad beddelayso: ")
        q = input("Geli tirada cusub: ")
        update_quantity(m, q)

    elif choice == "4":
        m = input("Enter magaca alaabta aad raadinayso: ")
        search_item(m)

    elif choice=="5":
        b=input("geli alaabta aad ka saarayso:")
        delete_item(b)

    elif choice == "6":
        total_stock()

    elif choice=="7":
        low_stock_check()



    elif choice == "8":
        print("\nWaad ku mahadsantahay isticmaalka barnaamijka. Macasalaama!")
        break

    else:
        print("\nFadlan dooro tiro u dhaxaysa 1 ilaa 7!")
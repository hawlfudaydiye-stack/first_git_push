expenses = [
  {"name": "food", "amount": 5},
  {"name": "transport", "amount": 3}
]

def add_expense(name,amount):
    if name and amount is not expenses:
        expense = {"name": name, "amount": amount}
        expenses.append(expense)

        print("waanu kaydinay si guul ah")
    else:
        print("xogtan hore loo kaydiyey")


# add_expense("qorsheeye",20)


def show_total():
    print(f"xogta  dic waa: {expenses}")

#

def delete_expense(name_to_delete):
    # 2. Loop ku dhex mara liiska
    for i in expenses:
        # 3. Hubi haddii magacu yahay kan aan rabno
        if i["name"] == name_to_delete:
            # 4. Halkan ayaa ah halka wax kasta lagu tirtirayo (Name + Amount)
            expenses.remove(i)
            print(f"Waanu tirtirnay '{name_to_delete}' iyo lacagtiisii oo dhan.")
            return  # Markay hal mar tirtirto ha joojiso loop-ka

    print("Kuma jiro magaca aad rabto inaad saarto")


def update(name):
    if name in expenses:


        print("")

def calculate_total():
    maran = 0
    for i in expenses:
        lacagta = i["amount"]

        maran += lacagta  # Halkan ayaa ah halka lagu keydinayo isku-darka

    print(f"Wadarta Guud ee lacagtuna waa: {maran}")  # Kan wuxuu soo baxayaa markuu loop-ku dhameystirmo

# calculate_total()
"""
    1. lacagta = i["amount"] (Soo-qabashada)
Xariiqan shaqadiisu waa "Kala-soocid".
Xusuuso in i uu yahay Dictionary u muuqda sidan: {"name": "food", "amount": 5}.
 Dictionary-gu waa sidii sanduuq dhowr waxyaabood ku jiraan.

Logic-ga: Waxaad Python ku leedahay: "Gudaha sanduuqa i, iska illow magaca (name),
 ee iisoo qabo oo kaliya qiimaha ku dhex jira sumadda (key) la yiraahdo "amount"."

Maxaa dhacaya?: Python waxay fureysaa sanduuqa, waxay soo saaraysaa nambarka (tusaale 5),
waxayna ku shubaysaa variable-ka cusub ee aad u bixisay lacagta.

Natiijada: Hadda lacagta waxay u taagan tahay nambar kaliya (sida 5 ama 3), ee ma ahan Dictionary dhan.

2. maran += lacagta (Isku-darka/Kaydinta)
Xariiqan shaqadiisu waa "Xusuusasho iyo Isku-geyn".
Calaamadda += waa mid aad u awood badan. Waxay ka dhigan tahay: maran = maran + lacagta.

Logic-ga: Waxaad Python ku leedahay: "Qaad nambarkii hore ugu jiray maran, ku dar lacagta cusub ee aad hadda soo qabatay, wadartoodana dib ugu rid isla sanduuqa maran."

Maxay muhiim u tahay?: Haddii aad dhihi lahayd maran = lacagta (oo kaliya), maran wuxuu iska illoobi lahaa lacagtii hore, wuxuuna xasuusan lahaa kaliya tii ugu dambaysay. Laakiin += waxay ka dhigaysaa inuu ururiyo (Accumulate) dhammaan lacagaha.
    
    """


def show_menu():
    print("\n==============================")
    print("MAAMULKA KHARASHKA (EXPENSE TRACKER)")
    print("1: Add (Ku dar)")
    print("2: View (Eeg)")
    print("3: Delete (Tirtir)")
    print("4: Total (Wadarta)")
    print("5: Exit (Kabax)")
    return input("Dooro (1-5): ")


# Loop-ka weyn ee barnaamijka socodsiinaya
while True:
    choice = show_menu()

    if choice == "1":
        user1 = input("Geli magaca kharashka: ")
        user2 = int(input("Geli inta ay tahay: "))
        add_expense(user1, user2)

    elif choice == "2":
        show_total()

    elif choice == "3":
        user1 = input("Geli magaca aad tirtirayso: ")
        delete_expense(user1)

    elif choice == "4":
        calculate_total()

    elif choice == "5":
        print("\nWaad ku mahadsantahay isticmaalka barnaamijka. Macasalaama!")
        break  # Kani wuxuu joojinayaa While Loop-ka

    else:
        print("\nFadlan dooro tiro u dhaxaysa 1 ilaa 5!")













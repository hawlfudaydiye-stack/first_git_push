import random
number_to_guess = random.randint(1, 100)

while True:
    try:
        # 1. Halkan waxaan u soo rignay koodka si uu try-ga u raaco
        choice = int(input("Geli nambar aad ku qiyaasto: "))

        # 2. 'if' wuxuu ka mid noqday try-ga (waa inuu gudaha u jiro)
        if choice < number_to_guess:
            print("Wuu ka waynyahay")
        elif choice > number_to_guess:
            print("Wuu ka yaryahay")
        else:
            print("Done! Waad soo saartay")
            break

    except ValueError:
        # 3. Except-ku hadda wuxuu la siman yahay try-ga
        print("Invalid number! Fadlan nambar sax ah geli.")



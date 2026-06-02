# 1. Layliga Koowaad: Function-ka Salaanta
# Abuur function la yiraahdo salaan_qof.
# Function-kani waa inuu magac ka aqbalaa qofka (argument), ka dibna daabacaa: "Haye [Magaca], soo dhawoow!".
# def salaan_qof(magac):
#     return f"soo dhawoow {magac}"
#
#
#
#
# print(salaan_qof("abdilahi jama"))




# def isku_dar(a,b):
#     return a+b
# natiijo=isku_dar(10,10)
# print(f"natiijadaadu waaa:{natiijo}")


# def isku_dar():
#     isku_gayn=int(input("pls enter number:"))
#     isku_gayn1 = int(input("pls enter another number:"))
#
#     return isku_gayn+isku_gayn1
#
#
#
# natiijo=isku_dar()
# print(f"natiijadaaadu waa = {natiijo}")


# 1. Qeex functions-ka xisaabta

# 1. Qeexidda Function-nada

def isku_dar(a, b):
    return a + b


def qaybi(a, b):
    if b == 0:
        return "Khalad: Ma qaybin kartid 0"
    return a / b


def dhufasho(a, b):
    return a * b


# 1. Function-ka weyn hal maraa la qeexaa
def main():
    print("\n--- MENU ---")
    print("1. Isku-dar")
    print("2. Qaybi")
    print("3. Isku-dhufasho")
    print("4. Ka bax (Exit)")

    doorasho = input("Dooro (1/2/3/4): ")

    # Haddii uu doorto inuu baxo
    if doorasho == "4":
        return "exit"

    if doorasho not in ["1", "2", "3"]:
        print("Invalid choice! Isku day markale.")
        return "continue"

    try:
        n1 = float(input("Gali nambarkii kowaad: "))
        n2 = float(input("Gali nambarkii labaad: "))

        if doorasho == '1':
            print(f"Natiijadu waa: {isku_dar(n1, n2)}")
        elif doorasho == '2':
            print(f"Natiijadu waa: {qaybi(n1, n2)}")
        elif doorasho == '3':
            print(f"Natiijadu waa: {dhufasho(n1, n2)}")

    except ValueError:
        print("Qalad: Fadlan nambar geli!")

    return "continue"


# 2. Loop-ka halkan ayuu ka bilaabanayaa (Bannaanka)
while True:
    status = main()
    if status == "exit":
        print("macasalaama")
        break  # Loop-ka jooji haddii qofku doorto 4
# Waa inaad u qaybisaa barnaamijka afar qaybood oo waaweyn:
# Ku darista (Add):
# Weydiiso isticmaalaha inuu soo geliyo magaca iyo lambarka.
# Hubi in magacu horey u jiray iyo in kale (si aan xog hore loo tirtirin).
# Haddii uusan jirin, ku dar dictionary-ga.
# 1. Waxaan abuuraynaa Dictionary la yiraahdo 'xogo' si xogta loogu kaydiyo
xogo = {"Axmed": "637718555"}

def add_xog(key, value):
    if key in xogo:
        print(f"Waan ka xunnahay, magaca {key} hore ayuu ugu jiray.")
    else:
        xogo[key] = value
        print(f"Waa lagu daray {key} si guul ah.")

def update_xog(key, value):
    if key not in xogo:
        print(f"Waanu ka xunnahay {key} kuma jiro diiwaanka.")
    else:
        # Kaliya xariiqan ayaa ku filan in nambarka la beddelo
        xogo[key] = value
        print(f"Si guul ah ayaa loogu update-gareeyey {key}.")

def Search_xogo(key):
    if key not in xogo:
        print("Magaca aad gelisay kuma jiro diiwaanka.")
    else:
        # Halkan waxaan soo bixinaynaa nambarka qofkaas kaliya
        print(f"Magaca: {key} | Nambarka: {xogo[key]}")

def main():
    print("\n--- MENU ---")
    print("1. xog ku dar")
    print("2. xog update gare")
    print("3. xog ka raadi")
    print("4. Ka bax (Exit)")

    doorasho = input("Dooro (1/2/3/4): ")

    if doorasho == '1':
        u = input("Geli magaca qofka: ")
        n = input("Geli nambarkiisa: ")
        add_xog(u, n)

    elif doorasho == '2':
        u = input("Geli magaca qofka la bedelaayo: ")
        p = input("Geli nambarka cusub: ")
        update_xog(u, p)

    elif doorasho == '3':
        u = input("Geli magaca aad raadinayso: ")
        Search_xogo(u)

    elif doorasho == '4':
        print("Macsalaama!")
        return # Barnaamijka wuu xirmayaa

# U yeer main()
main()




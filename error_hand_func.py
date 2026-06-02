def xisaabi_celceliska(magaca, dhibcaha):
    try:
        # 1. Xisaabi wadarta (sum)
        wadarta = sum(dhibcaha)

        # 2. Xisaabi tirada (len)
        tirada = len(dhibcaha)

        # 3. Qaybi: wadarta / tirada (Halkan ayuu ZeroDivisionError ka dhici karaa)
        natiijo = wadarta / tirada

        # 4. Soo celi natiijada
        return f"Ardayga {magaca} celceliskiisu waa: {natiijo}"

    except ZeroDivisionError:
        return "Khalad: Liisku waa maran yahay, ma jiro wax la xisaabiyo."

    except TypeError:
        return "Khalad: Fadlan dhibcaha ku soo rid liis (List) ay lambaro ku jiraan."

    finally:
        print(f"Baaritaanka xogta {magaca} waa dhammaaday.")


# --- TIJAABO ---
print(xisaabi_celceliska("Qorsheeye", [90, 50, 80]))
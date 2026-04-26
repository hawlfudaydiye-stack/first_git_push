# # Soo deji maktabadda 'random' si aan xubnaha password-ka ugu doorano si nasiib ah (randomly)
# import random
# # Soo deji maktabadda 'string' si aan u helno liiska xarfaha iyo calaamadaha adduunka
# import string
#
#
# # --- QAYBTA FUNCTIONS-KA ---
#
# # Function-kan shaqadiisu waa inuu abuuro password cusub
# # 'dhererka=12' waxay ka dhigaysaa haddii aan dherer la sheegin inuu 12 isticmaalo
# def generate_password(dhererka=12):
#     """Barnaamij soo saaraya password random ah"""
#
#     # 1. Data Structures: Halkani waa keydka xogta aan password-ka ka samaynayno
#     xarfo = string.ascii_letters  # Waxay koubaysaa dhammaan xarfaha (a-z iyo A-Z)
#     tirooyin = string.digits  # Waxay koubaysaa nambarada (0-9)
#     calaamado = string.punctuation  # Waxay koubaysaa calaamadaha sida (!, @, #, $, iwm)
#
#     # Isku dar dhammaan xogta kor ku xusan si ay u noqdaan hal barkad oo weyn
#     dhamaan = xarfo + tirooyin + calaamado
#
#     # 2. Logic:
#     # random.sample: Waxay barkaddaas ka dhex dooranaysaa tiro xarfo ah oo dhererka aan rabno ah
#     # "".join: Waxay isku dhejineysaa xarfahaas kala firdhisan si ay eray (string) u noqdaan
#     password = "".join(random.sample(dhamaan, dhererka))
#
#     # Gacanta ka saar (soo celi) password-ka la diyaariyey
#     return password
#
#
# # Function-kan shaqadiisu waa inuu baaro haddii password-ku adag yahay
# def validate_password(password):
#     """Barnaamij hubinaya in password-ku adag yahay"""
#
#     # Bilawga dhibcaha (score) waa eber, waxaana ku daraynaa mar kasta oo shuruud la buuxiyo
#     score = 0
#     # Liis madhan oo aan ku keydinayno talooyinka haddii password-ku daciif yahay
#     feedback = []
#
#     # Check 1: Hubi dhererka password-ka (Dhererka ugu yaraan waa 8)
#     if len(password) >= 8:
#         score += 1  # Haddii uu 8 ka weyn yahay, hal dhibic sii
#     else:
#         # Haddii uu ka yar yahay, taladan ku dar liiska feedback-ga
#         feedback.append("Waa inuu ka dheer yahay 8 xarfood.")
#
#     # Check 2: Hubi haddii uu nambaro leeyahay (any() waxay eegaysaa xaraf kasta)
#     if any(char.isdigit() for char in password):
#         score += 1  # Haddii hal xaraf xataa uu nambar yahay, hal dhibic sii
#     else:
#         feedback.append("Waa inuu ku jiraa ugu yaraan hal tiro (0-9).")
#
#     # Check 3: Hubi haddii uu xarfo waaweyn leeyahay (.isupper())
#     if any(char.isupper() for char in password):
#         score += 1  # Haddii hal xaraf xataa uu weyn yahay, hal dhibic sii
#     else:
#         feedback.append("Waa inuu ku jiraa ugu yaraan hal xaraf oo weyn (A-Z).")
#
#     # Soo celi wadarta dhibcaha iyo liiskii talooyinka ahaa
#     return score, feedback
#
#
# # --- QAYBTA ISTICMAALKA (MAIN LOGIC) ---
#
# print("--- PASSWORD HELPER ---")
#
# # 1. Wicitaanka Sameeyaha:
# # Waxaan u yeedhaynaa function-kii generate_password annagoo raba 14 xarfood
# cusub = generate_password(14)
# print(f"Password-ka laguu soo saaray: {cusub}")
#
# # 2. Wicitaanka Hubiyaha:
# # Waxaan u dhiibaynaa password-kii cusub si uu u soo baaro
# # Waxaan natiijada ku kala qabanaynaa laba variable: 'mark' iyo 'dardaaran'
# mark, dardaaran = validate_password(cusub)
#
# # 3. Go'aanka:
# # Maadaama aan 3 shuruudood hubinay, haddii dhibcuhu (mark) yihiin 3, waa "Strong"
# if mark == 3:
#     print("Darajada: Aad u adag (Strong! ✅)")
# else:
#     # Haddii kale waa daciif, waxaana loo baahan yahay in la soo saaro sababta
#     print(f"Darajada: Aad u daciif ah (Weak! ❌)")
#
#     # Loop-kani wuxuu mid mid u soo daabacayaa dhaliilihii ku jiray liiska 'dardaaran'
#     for f in dardaaran:
#         print(f"- {f}")


tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Dooro (1-4): ")

    if choice == '1':
        new_task = input("Qor hawsha cusub: ")
        tasks.append(new_task)
        print("Waa lagu daray!")

    elif choice == '2':
        print("\nHawlaha kuu qoran:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == '3':
        if tasks:
            num = int(input("Tirada hawsha aad tirtirayso: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Waxaad tirtirtay: {removed}")
            else:
                print("Number-kaas ma jiro!")
        else:
            print("Liisku waa maran yahay.")

    elif choice == '4':
        print("Macasalaama!")
        break
    else:
        print("Fadlan dooro 1 ilaa 4.")
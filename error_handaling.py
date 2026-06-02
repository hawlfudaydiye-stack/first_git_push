# 1. try block
# Halkan waxaad ku dhex qortaa koodka aad ka cabsi qabto inuu qalad keeno. Python waxay isku dayaysaa inay koodkan fuliso.
#
# 2. except block
# Haddii qalad (Exception) uu ku dhaco gudaha try, barnaamijku wuxuu u boodayaa qaybtan. Halkan ayaad ku qeexaysaa waxa la samaynayo haddii qalad dhaco.
#
# 3. else block (Optional)
# Qaybtan waxay fulaysaa oo kaliya haddii wax qalad ah uusan dhacin gudaha block-ga try.
#
# 4. finally block (Optional)
# Koodka halkan ku jira wuxuu fulayaa mar walba, iyadoo aan la eegin in qalad dhacay iyo in kale. Waxaa badanaa loo isticmaalaa in lagu xiro faylasha ama xiriirka database-ka.

# IndentationError
#
# try:
#     tijaabo_error_handaling=int(input("please enter number:"))
#     print(1/tijaabo_error_handaling)
# except ZeroDivisionError:
#     print("zero waxba loo ma qaybin karo! ")
#
# except ValueError:
#     print("enter only number!")
#
# except TypeError:
#     print("waxaad khaldan waa data type erorrs!")
#
# except Exception:
#     print("waxabaa khalda error jira ee hagaaji")
#



# Layliga 1-aad: Qabashada Qaladka IndexError
# Abuur barnaamij leh liis (list) ka kooban 3 magac. Weydii isticmaalaha inuu soo galiyo lambarka booska (index) uu rabo inuu arko. Haddii uu galiyo lambar ka weyn inta liiska ku jirta (tusaale 5), qabo qaladka oo u sheeg: "Raali ahow, booskaas waxba kuma jiraan."
#
# Tusaale koodh ah oo aad bilaabi karto:

#
# magacyada = ["Axmed", "Faadumo", "Cali"]
#
# try:
#     dooro_nambar= int(input("soo dooro nambar:"))
#     print(f"magaca aad soo doratay waa:{magacyada[dooro_nambar]}")
#
# except IndexError:
#     print("pls numabrka aad dooray kuma jiro list")
#
# except ValueError:
#     print("pls keliya numbar baa la oogalyahay!")



#  Isku-darka try, except, iyo finallySamee function la yiraahdo xisaabi_da('da() (calculate age):'
# ('Weydii isticmaalaha sanadkii uu dhashay.Haddii uu xarfo (text) soo galiyo, qabo ValueError.'
# 'Haddii uu lambar sax ah galiyo, xisaabi da'))diisa ($2024 - \text{sanadka}$).
# Dhamaadka barnaamijka (si kasta oo ay wax u dhacaan), daabac: "Waad ku mahadsantahay isticmaalka xisaabiyaha."

#
# def xisaabi_da():
#     try:
#         # 1. Weydiinta sanadka
#         sanadka_dhalashada = int(input("Geli sanadka aad dhalatay: "))
#
#         # 2. Xisaabinta (Sanadka hadda - sanadka dhalashada)
#         da_da = 2026 - sanadka_dhalashada
#
#         print(f"Da'daadu waa: {da_da}")
#
#     except ValueError:
#         # 3. Qabashada haddii xaraf la galiyo
#         print("Khalad: Fadlan lambar uun geli (tusaale: 1995).")
#
#     finally:
#         # 4. Farriinta ugu dambaysa ee mar walba fulaysa
#         print("Waad ku mahadsantahay isticmaalka xisaabiyaha.")
#
#
# # U yeer function-ka si uu u shaqeeyo
# xisaabi_da()



# Layliga 1-aad: "The Infinite Guard" (Loop iyo Try-Except)Samee barnaamij isticmaalaha weydiinaya inuu dhalo (input) lambar.
# Barnaamijku waa inuu ahaado mid aan istaageyn (Infinite Loop) ilaa uu isticmaalahu ka keeno natiijo sax ah.
# Shuruudaha:Haddii uu xarfo (text) galiyo, qabo ValueError oo u sheeg:
# "Ma ahan lambar, mar kale isku day."
# Haddii uu lambar sax ah galiyo, u xisaabi Square Root-ka lambarkaas ($n^2$ ama $n \times n$),
# ka dibna jooji barnaamijka (break).Isticmaal finally si aad u tiraahdo: "Isku daygaagu waa diiwaangashan yahay."

#
# while True:
#     try:
#         qorsheeye=int(input("geli nambar oo keliya!:"))
#
#         square_root = qorsheeye ** 0.5
#
#         print(square_root)
#         break
#
#     except ValueError:
#         print("pls only lanbar la ogalyahay!")
#
#     finally:
#         print("isku daygaagu waa diiwaangashan yahay")



'''
"The Safe Divider" (Multiple Exceptions)Samee function la yiraahdo qaybiye_amni_ah().
 Function-kani waa inuu aqbalaa labo lambar ($a$ iyo $b$).
 Shuruudaha:Haddii $b$ ay tahay 0, qabo ZeroDivisionError oo soo celi: "Khalad: Eber waxba looma qaybin karo.
 "Haddii mid ka mid ah xogta la siiyay aysan ahayn lambar (tusaale: xarfo),
  qabo TypeError oo soo celi: "Khalad: Labada dhinacba waa inay lambar yihiin."Haddii kale, soo celi natiijada saxda ah.

'''







def diiwaangeli_arday():
    while True:
        try:
            magaca = input("Geli magaca ardayga: ")
            da_da = int(input("Geli da'da ardayga: "))
            if da_da<=0:
            else:

        except ValueError:
            print("caqli gal maaha")

            # Halkan ku dar shuruudda (if statement) si aad u hubiso 0-120
            # Haddii ay khaldantahay isticmaal: raise ValueError("Fariintaada")

            print(f"Hambalyo! {magaca} waa la diiwaangeliyey.")
            break # Jooji loop-ka haddii wax walba sax yihiin

        except ValueError as e:
            # 'as e' waxay kuu ogolaanaysaa inaad daabacdo fariintii aad 'raise' gareysay
            print(f"Fadlan isku day kale: {e}")

# U yeer function-ka
diiwaangeli_arday()











# Abuur variable la yiraahdo calculateArea.
#
# U xilsaar (assign) function qaadanaya labo qimtimo (parameters): length iyo width.
#
# Function-ku waa inuu soo celiyo (return) natiijada marka la isku dhufto labadaas tiro.
#
# U yeer function-ka adigoo isticmaalaya variable-ka, kuna dhex daabac


# def calculateArea(length , width):
#     return length*width
#
# lugu_kaydiyay_vr=calculateArea
# print(lugu_kaydiyay_vr(10,2))
# print(lugu_kaydiyay_vr is calculateArea)


#
# Abuur variable la yiraahdo toCelsius.
# U xilsaar function qaadanaya hal qiimo oo ah fahrenheit.
# Formula-da loo isticmaalo waa: $(F - 32) \times \frac{5}{9}$.
# Isku day inaad u yeerto adigoo isticmaalaya variable-ka oo u dhiibaya qimaha 68 (waxay kuu soo celinaysaa 20).

# def heer_kulka(fahrenheit):
#     # Waxaan ku daray qaansooyin si xisaabtu u saxanto
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius
#
# # Natiijada function-ka ayaan soo daabacaynaa
# natiijada = heer_kulka(68)
# print(natiijada)
#
# # Ama si toos ah:
# # print(heer_kulka(68))



# Abuur function la yiraahdo is_even(n)
# oo soo celinaya True haddii lambarku yahay dhow (even).
# Kadib, isticmaal function-kaas adigoo u dhiibaya filter() si aad liiska hoose uga soo saarto kaliya lambarrada dhowga ah.


# def is_even(n):
#     # Waxay soo celinaysaa True haddii haraagu yahay 0 marka 2 loo qaybiyo
#     return n % 2 == 1
# # waa odd
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # Halkan is_even ayaan u dhiibaynaa filter()
# imika = list(filter(is_even, numbers))
#
# print(imika)  # Output: [2, 4, 6, 8, 10]



#
# Jimicsiga 1aad: "Warshadda Salaamta"
# Waa inaad dhistaa function la yidhaahdo sameey_salaan.
#
# Function-ka weyni (sameey_salaan) waa inuu qaataa luuqadda (tusaale: "Maalin wanaagsan" ama "Hello").
#
# Function-ka yar (salaan_shakhsi) waa inuu qaataa magaca qofka.
#
# U dambayn, waa inuu soo celiyo labadii oo isku xidhan.
#
# Koodhka ka maqan buuxi:



def sameey_salaan(luuqad):
    def salaan_shakhsi(magac):

        return f"{luuqad},{magac} "
    return salaan_shakhsi

salaan=sameey_salaan("hello")
print(salaan("qorsheeye"))













































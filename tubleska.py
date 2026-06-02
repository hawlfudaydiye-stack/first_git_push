# user_info = ["Axmed", 21, "AI Developer", "Somalia"]
#
# # Waxaan rabnaa magaca iyo shaqada oo kaliya
# magac, _, shaqo, _,wadan = user_info
#
# print(magac) # Axmed
# print(shaqo) # AI Developer
# print(wadan)



#
# Sidee ayaad hal xariiq ugu dhex qabsan kartaa lambarka 10
# variable la yiraahdo x iyo lambarka 30 variable la yiraahdo z, adigoo iska indho-tiraya 20-ka?

# coordinates = (10, 20, 30)
# x, _,z=coordinates
# print(x,)
# print(z)




# Haddii aad haysato Tuple-ka soo socda oo ah xogta server-ka:
# U samee unpacking oo soo saar IP-ga (midka u horreeya) iyo Status-ka (Online).
#
# Xogta kale oo dhan (Admin, Password, Version) ku ururi hal variable oo la yiraahdo other_details.

# server_info = ("192.168.1.1", "Admin", "P@ssword123", "Online", "v2.4")
# ip,*igaxidh,online=server_info
# print(ip)
# print(online)
# print(igaxidh)



# Halkii aad dhihi lahayd arday = ["Axmed", 21] (ma garanaysid 21 waxay tahay)
# arday = {"magac": "Axmed", "da_da": 21}
#
# print(arday["magac"],arday["da_da"])  # Natiijada: Axmed

d = {"name": "Kat", 1: "Python"}

print(d["nme"])      # "Kat"
print(d.get(2))   # None (Error ma dhacayo inkastoo "age" aysan jirin)











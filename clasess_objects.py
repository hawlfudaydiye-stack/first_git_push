# 1. Qeexidda Class-ka (Naqshadda)
class Arday:
    # 'Constructor' waa meesha lagu qeexo sifooyinka arday kasta yeelanayo
    def __init__(self, magaca, aqoonsiga, darajada):
        self.magaca = magaca        # Sifada 1: Magaca
        self.aqoonsiga = aqoonsiga    # Sifada 2: ID-ga
        self.darajada = darajada    # Sifada 3: GPA ama Darajada

    # Method (Ficil): Midkani wuxuu daabacayaa macluumaadka ardayga
    def tusi_xogta(self):
        print(f"Magaca: {self.magaca} | ID: {self.aqoonsiga} | Darajada: {self.darajada}")

    # Method (Ficil): Midkani wuxuu sheegayaa in ardaygu gudbay iyo in kale
    def ma_gudbay(self):
        if self.darajada >= 50:
            return f"{self.magaca} waa uu gudbay! 🎉"
        else:
            return f"{self.magaca} wuu dhacay. 📚"

# ---------------------------------------------------------
# 2. Samaynta Objects (Shayadii rasmiga ahaa)

# Waxaan abuuraynaa labo arday oo kala duwan laakiin ka yimid hal Class
arday1 = Arday("Axmed Cali", "ID001", 85)
arday2 = Arday("Hani Maxamed", "ID002", 45)

# 3. Adeegsiga Object-yada (Calling Methods)
print("--- Macluumaadka Ardayda ---")
arday1.tusi_xogta()
print(arday1.ma_gudbay())

print("\n--- Macluumaadka Ardayda ---")
arday2.tusi_xogta()
print(arday2.ma_gudbay())

# define a class
class Dog:
    sound = "bark"  # class attribute

class Dog:
    sound = "bark"

dog1 = Dog() # Creating object from class
print(dog1.sound) # Accessing the class



class Dog:
    # 1. CLASS ATTRIBUTE:
    # Tani waa sifo guud. Eey kasta oo la abuuro waa "Canine" (nooca eeyaha).
    species = "Canine"

    # 2. THE __INIT__ METHOD (Constructor):
    # Waa mishiinka shaqada bilaaba marka aad leedahay Dog(...).
    # 'self' waxay u taagan tahay eeyga hadda gacanta lagu hayo.
    # 'name' iyo 'age' waa xogta aad dibadda ka keenayso.
    def __init__(self, name, age):
        # 3. INSTANCE ATTRIBUTES:
        # Halkan waxaan xogta dibadda ka timid ku xiraynaa eeyga.
        self.name = name  # "Magaca eeygan hadda la sameeyey ka dhig 'name'"
        self.age = age  # "Da'da eeygan hadda la sameeyey ka dhig 'age'"


# 4. CREATING AN OBJECT (Abuurista eey gaar ah):
# Marka aad line-kan qorto, Python waxay dhex gashaa __init__
# Waxayna 'Buddy' u dhiibtaa name, 3-na waxay u dhiibtaa age.
dog1 = Dog("Buddy", 3)

# 5. ACCESSING DATA (Xog soo saaris):
print(dog1.name)  # Waxay soo saaraysaa: Buddy (Magaca eyga koowaad)
print(dog1.species)  # Waxay soo saaraysaa: Canine (Sifada guud ee eeyaha)

class Student:
    school_name = "Somali National University"

    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
Student1=Student("abdiahi jama ahmed","C+")

print(Student1.name)
print(Student1.grade)
print(Student1.school_name)














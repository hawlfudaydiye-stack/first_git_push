# class BankAccount:
#     bank_name = "Iftin Bank"
#
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     # 1. Method-ka lacag dhigista
#     def deposit(self, amount):
#         self.balance += amount  # Waxaan ku darnay lacagtii cusbayd
#         print(f"Waxaad dhigatay ${amount}. Lacagtaada hadda waa ${self.balance}.")
#
#     # 2. Method-ka lacag kala bixista
#     def withdraw(self, amount):
#         if amount > self.balance:
#             # Haddii lacagta la rabo ay ka badantahay inta kuu taal
#             print("Lacag ku filan kuguma jirto!")
#         else:
#             # Haddii kale, ka jaro balance-ka
#             self.balance -= amount
#             print(f"Waxaad la baxday ${amount}. Waxaa kuu haray ${self.balance}.")
#
# # --- TIJAABADA KOODKA ---
#
# # 1. Abuuro koonto uu leeyahay Farah oo leh $100
# my_account = BankAccount("Farax", 100)
#
# # 2. Ku dar $50
# my_account.deposit(50)
#
# # 3. Isku day inaad la baxdo $200 (Waa inay diiddaa)
# my_account.withdraw(200)
#
# # 4. Isku day inaad la baxdo $40 (Waa inay oggolaataa)
# my_account.withdraw(40)

class Library:
    def __init__(self, library_name): # Halkan 'books' waan ka saarnay
        self.library_name = library_name
        self.books = []  # Liis maran oo buugaagta loogu talagalay

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Maktabada waxaa lagu soo daray buuga: {book_name}")

    def show_books(self): # Hal mar oo nadiif ah
        # 1. Hubi haddii liisku uu madhan yahay
        if len(self.books) == 0:
            print("Maktabaddu waa faaruq, wax buug ah kuma jiraan.")
        else:
            # 2. Isticmaal 'for loop' si aad u soo saarto
            print(f"\nLiiska buugaagta yaalla {self.library_name}:")
            for buug in self.books:
                print(f"- {buug}")

# --- TIJAABADA ---
# Hadda 'library_name' oo kaliya ayaan siinaynaa
my_lib = Library("Maktabadda Qaranka")

my_lib.add_book("Hayaan")
my_lib.add_book("Aqoondaro waa u nacab")

# U yeer method-ka si uu noo tuso liiska
my_lib.show_books()












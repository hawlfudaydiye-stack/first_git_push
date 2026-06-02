# class Employee:
#     def __init__(self, name, salary):
#         self.name = name          # public attribute
#         self.__salary = salary    # private attribute
#
#     def accsess_salary(self):
#      return self.__salary
#
# emp = Employee("Fedrick", 50000)
# print(emp.name)
# print(emp.accsess_salary())


# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.__grade=grade
#
#     def update_grade(self, hubi):
#
#         if hubi > 0 and (self.__grade + hubi) <= 100:
#             self.__grade += hubi
#             print("Grade updated successfully")
#             print(f"Total grade is: {self.__grade}")
#         elif  hubi<= "-":
#             print("mines lama gaadhi karo pls hagaaji grades ka")
#
#         else:
#             print("Invalid update! Grade cannot exceed 100")
#
#
#
#     def accsess_grade(self):
#         return self.__grade
#
# arday1=Student("abdilahi jama",80)
# print(arday1.name)
#
# print(arday1.accsess_grade())
#
# arday1.update_grade(11)






















# # Bank Account class
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner          # public → qof walba wuu arki karaa
#         self.__balance = balance    # private → lama arki karo si toos ah
#
#     # Method lagu arko balance (controlled access)
#     def get_balance(self):
#         return self.__balance
#
#     # Method lacag lagu daro
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Deposit successful")
#         else:
#             print("Invalid amount")
#
#     # Method lacag lagala baxo
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient funds")  # lacag kuma filna
#         elif amount <= 0:
#             print("Invalid amount")
#         else:
#             self.__balance -= amount
#             print("Withdrawal successful")
#
#
#
# # object abuur
# account1 = BankAccount("Ali", 100)
#
# # public data
# print(account1.owner)  # ✔️ waa la arki karaa
#
# # private data (toos looma heli karo)
# # print(account1.__balance) ❌ ERROR
#
# # sax → isticmaal method
# print("Balance:", account1.get_balance())
#
# # lacag ku dar
# account1.deposit(50)
#
# # lacag kala bax
# account1.withdraw(30)
#
# # markale eeg balance
# print("New Balance:", account1.get_balance())
#
#




class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private (Lama arki karo bannaanka)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Waxaad ku dartay ${amount}")

    def get_balance(self):
        return f"Lacagta kuu hartay waa: ${self.__balance}"

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
# print(account.__balance) # Tani Error ayay bixinaysaa (waa xiran tahay)
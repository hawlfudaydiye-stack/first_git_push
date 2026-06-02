

import random
doorasho=('x','w','m')

while True:
 user_choice=input("choice only one?(x/w/m):").lower()
# if choice !='x' and choice!='w' and choice !='m':
 if user_choice not in doorasho:
    print("invlaid choice")

 computer_choice=random.choice(doorasho)
 print(f"adigu waxaad dooratay:{user_choice}")
 print(f"computarku waxa u doory:{computer_choice}")

 if user_choice==computer_choice:
    print("waa tie")

 elif(
    (user_choice=='x' and computer_choice=='m') or
    (user_choice=='m' and computer_choice=='w') or
    (user_choice=='w' and computer_choice=='x')):


    print("you win")
 else:
    print("computer win")

 masii_wadaysaa=input("ma sii wadaysaa: (y/n)")
 if masii_wadaysaa=='n':
  break





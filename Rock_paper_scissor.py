# Rock , paper , scissor game

import random

while True :
     a1=int(input('''
Game starts :
1 Enter
2 Exit
'''))
     if a1==1 :
         pass
     elif a1==2 :
         break
     uc=int(input('''
     Select your choice
     1 rock 
     2 paper 
     3 scissor
     '''))
     if uc==1 :
         print("Your choice : rock ")
     elif uc==2 :
         print("Your choice : paper ")
     elif uc==3 :
         print("Your choice : scissor ")
     l = ["rock", "paper", "scissor"]
     b = random.choice(l)
     print("Computer's choice : ", b)

     if uc == 1:
         if b == "rock":
             print("Match tie")
         elif b == "paper":
             print("Computer wins")
         else:
             print("You win")

     if uc == 2:
         if b == "rock":
             print("You win")
         elif b == "paper":
             print("Match tie")
         else:
             print("Computer win")

     if uc == 3:
         if b == "rock":
             print("Computer win")
         elif b == "paper":
             print("You win")
         else:
             print("Match tie")


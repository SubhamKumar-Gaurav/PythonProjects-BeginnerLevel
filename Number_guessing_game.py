# Number guessing game in Python (Using Random Module)

import random
x=random.randint(1,100)

y=int(input("Enter your number : "))
print("Number by computer : " , x)

if y<x :
    print("Your guess is low")
elif y>x :
    print("Your guess is high")
else :
    print("Congrats , your guess is right")

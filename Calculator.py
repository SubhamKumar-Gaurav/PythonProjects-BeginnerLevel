# Simple Calculator

print('''
+ add
- subtract 
* multiply 
/ 
''')

num1 = int(input("Enter the 1st value : "))
num2 = int(input("Enter the 2nd value : "))
opr = input("Enter the operator ( +,-,*,/ ) : ")

if opr=="+" :
    print("Answer : ", num1 + num2)
elif opr=="-" :
    print("Answer : ",num1 - num2)
elif opr=="*" :
    print("Answer : ",num1 * num2)
elif opr=="/" :
    print("Answer : ",num1 / num2)
else :
    print("Invalid operator")


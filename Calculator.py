Num1 = int(input("Enter First number: "))
Num2 = int(input("Enter Second number: "))
print("For Addtion press 1")
print("For subtraction press 2")
print("For multiplication press 3")
print("For Division press 4")
Command = str(input())

def Add():
    print(Num1+Num2)

def Sub():
    print(Num1-Num2)

def Mul():
    print(Num1*Num2)

def Div():
    print(Num1/Num2)

if "1" in Command:
    Add()
if "2" in Command:
    Sub()
if "3" in Command:
    Mul()
if "4" in Command:
    Div()


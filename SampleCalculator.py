# Simple Calculator with Functions
# Problem: Extend the simple calculator project to include the modulus operation. 
# Update the menu to include this option.


def add( x , y ):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def modulas(x,y):
    return x % y

print("Enter your Operation")
print(" 1. Add ")
print(" 2. Substract ")
print(" 3. Multiply ")
print(" 4. Divide ")
print(" 5. Modulus ")

choice = input("Enter your choice (1,2,3,4,5)")

num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

if choice == '1':
    print(f"{num1} + {num2} = add{(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = sub{(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = multiply{(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = divide{(num1, num2)}")
elif choice == '5':
    print(f"{num1} % {num2} = modulus{(num1, num2)}")
else:
    print("Invalid input")
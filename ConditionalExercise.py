#Conditional Statements
#Problem: Write a program that checks if a number entered by the user is 
#positive, negative, or zero and prints the result.

num = input("Enter a Number:")

if num == 0:
    print("Entered number is zero")
elif num > 0:
    print("Entered number is positive")
else:
    print("Entered number is negative")
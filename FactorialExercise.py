# Function for Factorial
#Problem: Write a function that calculates the factorial of a given number. 
#Call the function with a few different numbers and print the results.

def fact(n):
    if (n == 0 or n == 1):
        return 1
        print("Factorial of the number is 1")
    else:
        return n * fact(n-1)
        print("Factorial for the given number is", n)
    
#input("Enter the number")
print(f"{5} = fact(5)")
fact(5)   
#comment
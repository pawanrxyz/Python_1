def factorial(no):
    if no>1:
        return no*factorial(no-1)
    else:
        return 1
n = int(input("Enter any number for factorial:"))
print("Factorial of ",n,"is",factorial(n))
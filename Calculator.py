from ast import operator
from bdb import effective


first = input("Enter your first number")
operator = input("operator (+,-,*,/,% :)")
second = input("Enter your second number")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid operator")

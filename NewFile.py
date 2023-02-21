num = int(input("Enter any number:"))

Sum = 0
while num>0:
    rev = num%10
    Sum = Sum+rev
    num = num//10
print("Sum of digits:",Sum)
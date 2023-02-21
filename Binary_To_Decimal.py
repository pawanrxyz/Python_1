num = int(input("Enter any Decimal number"))
t = num
str1 = ''

while(t>0):
    r = t%2
    t = t//2
    # str1 = r+str1 
print("Decimal Equivalent of",num," is ",str1)

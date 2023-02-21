n = int(input("Enter any number:"))
rev = n
reve = 0

while(n>0):
    rev = rev%10
    reve = (reve*10)+rev
    n = n//10
if(rev==reve):
    print("This number is palindrome")
else:
    print("This number is not palindrome")
# print(reve)
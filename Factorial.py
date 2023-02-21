# n = int(input("Enter any number:"))
# fact = 1
# i = 1

# while(i<=n):
#     fact = fact*i
#     i = i+1
# print("The Factorial of ",n," is = ",fact)

# print factorial using for loop
num = int(input("Enter any number:"))
fact = 1
# for i in range(1,num+1):
for i in range(num,0,-1):
    fact = fact*i
print(fact)

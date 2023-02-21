def fib(a,b,n):
    if n==0:
        return
    c = a+b
    print(c)
    fib(b,c,n-1)
a = 0
b = 1
print(a)
print(b)
n = 7
print("Fiba: ",fib(a,b,n-2))
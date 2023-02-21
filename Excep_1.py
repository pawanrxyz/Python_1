a = int(input("Enter a number:"))
b = int(input("Enter second b number:"))

try:
    c = a/b
    print(c)
except:
    print("do not put zero in denimenator:")
else:
    print("This is else block")
finally:
    print("This is finally block")


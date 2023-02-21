a = 23
if a>30:
    print("This is the if body")
print("This is outside the if block")

i = 20
if i%2==0:
    print("This is the if block")
    print("i is an even number")
else:
    print("This is the else block")

c = 21  #--> c = 50
if c<25:
    if c%2==0:
        print("c is an even number less 25")
    else:
        print("c is an odd number less than 25")
else:
    print("c is greater than 25")

var = 'z'
if var=='a':
    print("this is the vowel a")
elif var=='e':
    print("This the vowel e")
elif var==i:
    print("This is the vowel i")
elif var=='o':
    print("This is the vowel o")
elif var=='u':
    print("This is the vowel u")
else:
    print("This is a constant")
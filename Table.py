num = int(input("Enter The number"))
for i in range(1,11):
    # print(str(num) + "X" +str(i) + " = " + str(i*num))

    #using f string 
    print(f"{num}X{i}={num*i}")
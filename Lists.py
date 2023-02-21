name = ["Akash","ajaay","Pawan","Aman","Avinash",56]
print(name)
numbers = [3,5,8,6,2,1]

numbers.remove(5)
# print(numbers) #Value remove from at any index
numbers.pop() #ccurrent add value remove
# print(numbers)
numbers.sort()
numbers.reverse()
# print(numbers)
# print(numbers[1:5: -3])
# print(len(numbers))
numbers.append(2) #append value add  in end
# print(numbers)

numbers.insert(1,4)  #add at any index
# print(numbers)

numbers[1] = 93 #use for change index value
# print(numbers)

#mutable means can change like list can be change
#immutable means can not cahange like tuple tp

# tp = (1,2,3) #this is tupple
tp = (1,)
# tp[1] = 5
print(tp)

#swap
a = 6
b = 3
# temp = a
# a = b
# b = temp
# print(a,b)

#swap with using python trick
a,b = b,a
print(a,b)

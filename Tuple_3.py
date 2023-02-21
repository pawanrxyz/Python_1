emp = ()
print(type(emp))

city = "pune",
print(type(city))
print("pune",)
city = "pune","lucknow","mumbai","haryana"
print(city)

print(city[1])
print(city[-1])
num = 1,2,3
print(city+num)
nest = (city,num)
print(nest)
rep = ("python",)*5 
print(rep)
rep = ("python",)
print(rep*10)
print(num[1:])
print(num[::1])
a,b,c,d = 1,2,3,4
print(a,b,c,d)

a,*b,c = num
print(a,b,c)
tuple1 = (1,2,3,4)
# print(tuple1)
# del tuple1
# print(tuple1)

#some built function
num1 = (3,3,2,2,2,2,5,6,4)
# num1.count(2)
print(num1.count(2))
print(max(num1))
print(min(num1))
print(sum(num1))
print(len(num1))

lst = [1,2,3,4]
print(type(lst))
tpl = tuple(lst)
print(tpl)
print(type(tpl))

lst = [(1,2,3),(4,5,6)]
print(lst)
lst.append(("Tuple","Inside","list"))
print(lst)

lst.remove((1,2,3))
print(lst)

tpl = (['a','b','c'],['d','e','f'])
print(tpl)
tpl[0].append("z")
print(tpl)
tpl.append[()]  # type: ignore

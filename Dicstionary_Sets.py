from re import S

d1 = {}
print(d1)
print(type(d1))
d2 = {1: "Welcome",2: "To",3: "Python",4: "tutorial"}
print(d2)
d3 = {"name": "Pawan","age": "19", "profession": "studendt"}
print(d3)

d4 = dict({1: "Welcome", 2: "to",3: "python",4: "tutorial"})
print(d4)
d5 = dict([(1,"welcome"),(2,"to"),(3,"python"),(4,"tutorial")])
print(d5)
d6 = {"name":{"first":"sam","last":"crew"},"age":19,"profession":"student"}
print(d6)

d7 = {}
d7[0] = "welcome"
print(d7)
d7[1] = ("How","are","you")
print(d7)
d7["name"] = "raj"
print(d7)
d7["name"] = {"first":"sam","last":"crew"}
print(d7)
#access elements
print(d7["name"])
print(d7["name"]["first"])
print(d7.get(1))
#delete elements
d7.pop(0) 
print(d7)
d7.popitem() #--> this method delete the last item
print(d7)
d7.values()
print(d7)

d8 = {"name":"anjali","role":"23","profession":"students"}
# print(d8)
print(d8.clear())

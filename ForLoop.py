#for i in range(5):
 #   print(i+1)
marks = [12,34,45,56]
print(marks[0])
print(marks[-1])
print(marks[0:2])
marks.append(99)
print(marks)

marks.insert(0,(78))
print(marks)
#checks value exits or not

print(78 in marks)
# find length
print(len(marks))

# length find though loop

i = 0
while i <len (marks):
  print(marks[i])
  i = i+1

  # To clear the list

  marks.clear
  print(marks)
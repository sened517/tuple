#Creating a tuple.
numbers=(10,20,30,40,50)
print(numbers)

#Accesing items using index
print(numbers[0])
print(numbers[3])

# tuple can not be modified
#numbers[0]=11
#print(numbers)

#len() function to find the numbers of items
print("The number of items are",len(numbers))

#iterate through a truple
colors=("red","green","purple","yellow","white")
for i in colors:
    print(i)

#check if an item exists in tuple
print("yellow"in colors)
print("brown"in colors)

#delete a tuple

names=("Jhon","Joe","Shawn","Tim","Aron")
#del names
#print(names)

#slicing

t=(10,20,30,40,50,60,70,80,90,100)
print(t[0:5])
print(t[1:5])
print(t[4:6])
print(t[0:])
print(t[:10])




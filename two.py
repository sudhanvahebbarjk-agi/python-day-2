mySet = {"apple", "banana", "cherry"}
print(type(mySet))
mySet.add("mango")
print(mySet)
mySet.remove("banana")
print(mySet)
newSet=mySet.copy()
print(newSet)
newSet.pop()

diffSet=newSet.difference()
print(diffSet)

myset=newSet.difference_update()
print(mySet)

mySet.clear()
print(mySet)
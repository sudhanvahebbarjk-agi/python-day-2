vegetables=["potato","onion","tomato"]

newlist=[i for i in vegetables if "p" in i]
print(newlist)

vegetables.append("carrot")
print(type(vegetables))

newlist=vegetables.copy()
print(vegetables.count("carrot"))

print(vegetables.index("potato"))
vegetables.insert(1,"radish")

vegetables.reverse()
print(vegetables)

vegetables.clear()

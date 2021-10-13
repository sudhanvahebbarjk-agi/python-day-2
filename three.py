thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict))
print(thisdict.get("brand"))
print(thisdict.items())
print(thisdict.keys())
print(thisdict.values())

newdict={}
newdict=thisdict.copy()
print(newdict)

thisdict.pop("year")
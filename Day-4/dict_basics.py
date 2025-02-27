dict1={"nil":"123",
       "admin":"admin",
       "default":"default",
       "hjsd":"dvkjd"}

dict2={"ygyef":"vdvd"}

print(dict1.get("nil"))
print(dict1.keys())
print(dict1.values())
print(dict1.popitem())
print(dict1.pop("default"))
print(dict1.fromkeys(["sarkar"],"abcd"))
print(dict1.items())
dict1.update(dict2)
print(dict1)

# dict1.clear()

print(dict1)
print(dict1.setdefault("huygh", "dfs"))
print(dict1)

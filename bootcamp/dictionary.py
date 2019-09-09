dict1={ "a":1, "b":2, "c":3 }
print(dict1)
print(dict1["b"])

dict1["d"]=4
print(dict1)
print("e" in dict1.keys())
print(5 in dict1.values())

dict1.setdefault("e",5)
print(dict1)
print("e" in dict1.keys())
print(5 in dict1.values())

dict1.pop("b")  #del dict1["b"]
print(sorted(dict1.items()))


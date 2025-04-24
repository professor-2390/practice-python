# covers dictionaries
# used to store values in key value pairs

dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(type(dict1))
print(len(dict1))

# can't use index (e.g. 0) we will have to specify k
print(dict1["a"])
print(dict1.get("a"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

# doesn't allow duplicates
# however add new items
dict1["d"] = 4
print(dict1)

dict1["a"] = 0
print(dict1)

dict1.update({"a": 1})
print(dict1)

# we can use pop function also del

# empty dictionaries
dict2 = {}
print(dict2)

dict3 = dict()
print(dict3)
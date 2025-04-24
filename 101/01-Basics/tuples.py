# covers tuples
# good when you know values won't be changed

tuple_items = ("item1", "item3", "item4")
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3, 4)
print(tuple_numbers)
print(type(tuple_numbers))

tuple_repeat = ("Combine!",) * 4
print(tuple_repeat)
print(type(tuple_repeat))


mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)
print(type(mixed_tuple))

# we can't append in tuple but we can combine
tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))

# unpack them
item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

# evaluate
print("item2" in tuple_items)

# index 
print(tuple_items.index("item1"))

tuple_items = ("item1", "item2", "item3")
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

print(len(tuple_items))

# last item
print(tuple_items[-1])
print(tuple_items[-2])

# slices to extract number of elements from the start to the end
print(tuple_items[0:2])
print(tuple_items[:2]) # except
print(tuple_items[-3:-1])

string1 = "I am a string!"
print(string1[0:4])
print(string1[-1])
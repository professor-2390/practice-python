# covers basic variables and data types

name = "professor"
print(name)

name_length = 9
print(name_length)

# redefined
name, name_length = "professor2", 10

# types
print(type(name))
print(type(name_length))

# casting
name_length = int("4")
print(name_length, type(name_length)) # 4 <class 'int'>

# these are two different variables
name_length = 9
Name_length = 10

print(name_length) # 9
print(Name_length) # 10

# lists
name_list = ["professor", "professor-2390"]
print(type(name_list))

# assigning 
name1, name2 = name_list
print(name1)
print(name2)

# tuple
name_tuple = ("professor", "professor-2390")
print(type(name_tuple))

# dictionary
name_dictionary = {"professor": 2, "professor-2390": 3}
print(type(name_dictionary))

# boolean
name_boolean = False
print(type(name_boolean))

# range 
name_range = range(9)
print(type(name_range))

# bytes
name_bytes = b"professor"
print(type(name_bytes))

print(name_tuple)
print(name_list)
print(name_dictionary)
print(name_boolean)
print(name_bytes)

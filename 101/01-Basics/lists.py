# covers lists
# lists are ordered and changeable

list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

# different datatypes
list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]
print(list2)
print(type(list2))

print(list1[0])
print(list1[-1])
print(list2[3][0])
print(list2[3][-1])

list1[0] = "X"
print(list1)

# delete
del list1[0]
print(list1)

# insert
list1.insert(0, "A")
print(list1)

del list1[0]
print(list1)

list1 = ["A"] + list1
print(list1)

list1.append("G")
print(list1)

print(max(list1))
print(min(list1))

# index of item
print(list1.index("C"))
print(list1[list1.index("C")])

list1.reverse()
print(list1)

# slice syntax notation starts from the end to the start with each element
list1 = list1[::-1]
print(list1)

# others
print(list1.count("A"))

list1.pop()
print(list1)

# extending
list3 = ["H", "I", "J"]
list1.extend(list3)
print(list1)

# remove all values
list1.clear()
print(list1)

# sort
list4 = [9, 3, 21, 1, 54, 6]
print(list4)

list4.sort()
print(list4)

# reverse sort
list4.sort(reverse=True)
print(list4)

# can't copy a list list2 = list1 list2 is a reference not a new copy 
# any changes made to this will be made to both because they share underlying data
list5 = list4
print(list4)
print(list5)

list5[3] = "X"
print(list5)
print(list4)

# both of them will have their 3rd index changed they point to same data
# to make changes to specific list we must copy it
list6 = list4.copy()
print(list4)
print(list6)

list6[3] = "Y"
print(list4)
print(list6)

# map function
list7 = ["1", "2", "3"]
print(list7)

# apply float cast to every item
list8 = list(map(float, list7))
print(list8)
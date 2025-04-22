# this covers string formatting

string1 = "I am a string!"
string2 = 'I am a string too!'

print(string1)
print(string2)

string3 = """I am a long
long
string!"""

print(string3)

string4 = "I\"m a string"
print(string4)

string5 = 'I"m a string'
print(string5)

string6 = "I\"m a string\nI\"m on a new line!"
print(string6)

string7 = "a" * 10
print(string7)

# prints length
print(len(string7))

# identify if certain item is in string
print("string" in string4) # True
print("professor" in string4) # False

# starts with
print(string4.startswith("I")) # True

# index
print(string4.index("string"))

# cases
print(string4.upper())
print(string4.lower())

# messy strings
messy_string = "   Messy string!"
print(messy_string)
print(messy_string.strip())

print(messy_string.replace("!", "?"))
print(messy_string.replace("string", "example"))

# split into multiple strings
print(messy_string.split())
print(messy_string.split(","))
print(messy_string.split())

# justification
print(string4.ljust(25))
print(string4.ljust(25, "X"))

print(string4.rjust(25))
print(string4.rjust(25, "X"))

# concatenate numbers with string
print("I am " + "a string")
print("String 4 is " + str(len(string4)) + "characters long")

print(1 + 1)
print("1" + "1")
print(type("1" + "1"))

# placeholders
print("string 4 is {} characters long!".format(len(string4)))

print("{} {} {}".format(len(string4), 0.5, 0x12))

# specify order
print("{0} {2} {1}".format(len(string4), 0.5, 0x12))
print("{length}".format(length=len(string4)))

# f-strings
length=len(string4)
print(f"string4 is {length} characters long")

print(f"string4 is {length:.2f} characters long") # float
print(f"string4 is {length:.3f} characters long") # float
print(f"string4 is {length:.4f} characters long") # float

print(f"string4 is {length:x} characters long") # float
print(f"string4 is {length:b} characters long") # float
print(f"string4 is {length:o} characters long") # float

print("string4 is %d characters long!" % len(string4))
print("string4 is %f characters long!" % len(string4))
print("string4 is %x characters long!" % len(string4))

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

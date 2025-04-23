valid = True
not_valid = False

print(valid)
print(not_valid)

# operators
print(valid == True)  # if valid is True
print(not_valid == False)

print(valid != True)
print(not_valid != True)

# python short-hand syntax
print(not valid)
print(not not_valid)

print((10 < 9) == True)
print((10 == 9) == True)
print((10 != 9) == True)
print((10 >= 9) == True)
print((10 <= 9) == True)
print((10 > 9) == True)

# same result
print((10 < 9))
print((10 == 9))
print((10 != 9))
print((10 >= 9))
print((10 <= 9))
print((10 > 9))

print("--------")

# combine statements
print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)

# referenced as numbers
print(bool(0))
print(bool(1))

print(bool(0) == False)
print(bool(1) == True)

# evaluating arithmetic operations
print(10 + 10)
print(10 - 10)
print(10 / 10)
print(10 // 10)

print(10 / 3)  # smallest
print(10 // 3)  # largest

print(10 * 10)
print(10**10)  # power
print(10 % 10)  # modulus

x = 10
print(x)
x = x + 1
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)

x = 13
print(bin(x))
print(bin(x)[2:].rjust(4, "0"))

y = 5
print(bin(x))
print(bin(x)[2:].rjust(4, "0"))

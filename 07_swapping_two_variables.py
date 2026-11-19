x = 10
y = 20
print("Before:")
print("x =", x)
print("y =", y)

# method 1: python's tuple unpacking (the easy way)
x, y = y, x
print("After (tuple swap):")
print("x =", x)
print("y =", y)

# method 2: using a temporary variable (the classic way)
temp = x
x = y
y = temp
print("After (temp swap):")   # back to the original order
print("x =", x)
print("y =", y)
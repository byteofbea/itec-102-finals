# type conversion (casting) changes a value from one type to another

# str -> int
text_number = "100"
number = int(text_number)
print(number + 5)            # 105 (math works now)

# int -> float
print(float(7))              # 7.0

# float -> int (decimal part is cut off, not rounded)
print(int(9.99))             # 9

# int -> str (needed to join a number with text)
age = 25
print("I am " + str(age) + " years old")

# Anything -> bool (empty/zero is False, everything else is True)
print(bool(0), bool(""), bool("hi"), bool(5))
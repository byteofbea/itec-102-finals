name = "Sybela"
age = 18
program = "Computer Science"
price = 1234.5678

# an f-string starts with f and puts variables inside {}
print(f"My name is {name} and I am {age} years old.")

# you can run expressions inside the braces
print(f"In 5 years I will be {age + 5}.")

print(f"I am taking {program}.")

# format numbers: 2 decimal places, and thousands separator
print(f"Price: {price:.2f}")
print(f"Price: {price:,.2f}")

# align text: < left, > right, ^ center (width of 10)
print(f"[{name:<10}]")
print(f"[{name:>10}]")
print(f"[{name:^10}]")
# Comparison of two numbers
print("\n----- 2. Comparison of Two Numbers -----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Variation 1 : if - else
print("Using if-else:")
if a > b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than or equal to", a)

# Variation 2 : short hand if-else (ternary operator)
print("Using short hand if-else:")
print(a, "is greater") if a > b else print(b, "is greater or equal")

# Variation 3 : short hand if-else storing result in a variable
result = a if a > b else b
print("Greater number is:", result)
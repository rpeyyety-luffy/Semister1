# Find the sign of a number (num = -55)
print("\n----- 3. Sign of a Number -----")
num = -55

# Variation 1 : if - elif - else
print("Using if-elif-else:")
if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print("Number is Zero")

# Variation 2 : nested if-else
print("Using nested if-else:")
if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print(num, "is Positive")
else:
    print(num, "is Negative")

# Variation 3 : short hand (nested ternary)
print("Using short hand:")
sign = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(num, "is", sign)
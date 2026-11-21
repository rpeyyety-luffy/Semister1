# Find out whether a number is ODD or EVEN
print("----- 1. Odd or Even -----")
num = int(input("Enter a number: "))

# Variation 1 : using only 'if'
print("Using if:")
if num % 2 == 0:
    print(num, "is Even")
if num % 2 != 0:
    print(num, "is Odd")

# Variation 2 : short hand if (one-line if)
print("Using short hand if:")
if num % 2 == 0: print(num, "is Even")
if num % 2 != 0: print(num, "is Odd")

# Variation 3 : if - elif (if else if)
print("Using if-elif:")
if num % 2 == 0:
    print(num, "is Even")
elif num % 2 == 1:
    print(num, "is Odd")
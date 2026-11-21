# ----------------------------------------------------------
# Fibonacci series up to n terms
# ----------------------------------------------------------
print("\n----- 4. Fibonacci Series -----")
n = int(input("How many terms? "))

# Variation 1 : for loop
print("Using for loop:")
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Variation 2 : while loop
print("Using while loop:")
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count = count + 1
print()

# Variation 3 : using a list
print("Using list:")
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[:n])
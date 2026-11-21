
# ---------- Method 1 : Using 'and' operator ----------
a = 15
b = 25
c = 20
if (a >= b) and (a >= c):
    greatest = a
elif (b >= a) and (b >= c):
    greatest = b
else:
    greatest = c
print(f"The greatest number is: {greatest}")

# ---------- Method 2 : Short hand if...else ----------
a = 15
b = 25
c = 20
greatest = a if (a >= b and a >= c) else (b if b >= c else c)
print(f"The greatest number is: {greatest}")

# ---------- Method 3 : Using max() function ----------
a, b, c = 15, 25, 20
greatest = max(a, b, c)
print(f"The greatest number is: {greatest}")
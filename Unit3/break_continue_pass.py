# Program: Print numbers 1 to 10
# Variations: 1) break  2) continue  3) pass

# ---------- Variation 1 : break statement ----------
# loop stops completely when i becomes 6
for i in range(1, 11):
    if i == 6:
        break
    print(i, end="  ")
print()

# ---------- Variation 2 : continue statement ----------
# even numbers are skipped, only odd numbers are printed
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end="  ")
print()

# ---------- Variation 3 : pass statement ----------
# pass does nothing, so all numbers are printed
for i in range(1, 11):
    if i == 5:
        pass
    print(i, end="  ")
print()
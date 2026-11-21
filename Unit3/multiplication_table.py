# Program: Display the multiplication table of a number
# Variations: 1) while  2) while with break  3) while with continue  4) while with pass

# ---------- Variation 1 : While loop ----------
num = 5
count = 1
while count <= 10:
    print(f"{num} x {count} = {num * count}")
    count += 1

print()
# ---------- Variation 2 : While with break ----------
num = 5
count = 1
while count <= 10:
    if count == 6:
        print("Stopping table early!")
        break
    print(f"{num} x {count} = {num * count}")
    count += 1

print()
# ---------- Variation 3 : While with continue ----------
num = 5
count = 0
while count < 10:
    count += 1
    if count == 5:
        print(f"{num} x {count} = SKIPPED")
        continue
    print(f"{num} x {count} = {num * count}")

print()
# ---------- Variation 4 : While loop with pass ----------
num = 5
count = 1
while count <= 10:
    print(f"{num} x {count} = {num * count}")
    if count % 2 == 0:
        pass    # Placeholder: do nothing for even numbers
    else:
        pass    # Placeholder: do nothing for odd numbers
    count += 1
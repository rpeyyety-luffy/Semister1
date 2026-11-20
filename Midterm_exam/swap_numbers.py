# Program to swap two integers using temporary variable
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping: a =", a, ", b =", b)

temp = a   # keep value of a safely in temp
a = b      # put value of b in a
b = temp   # put old value of a into b

print("After swapping: a =", a, ", b =", b)
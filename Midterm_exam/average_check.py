# Program to find average of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
average = (a + b + c) / 3
if average >= 50:
    print("Average is at least 50")
else:
    print("Average is below 50")
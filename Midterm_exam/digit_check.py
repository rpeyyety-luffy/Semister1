# Program to check if string contains only digits
text = input("Enter a positive number: ")
if text.isdigit():
    number = int(text)
    print("Number =", number)
else:
    print("Invalid input")
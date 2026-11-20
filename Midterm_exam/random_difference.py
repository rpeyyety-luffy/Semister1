# Program to find difference between random number and user's number
import random
number = random.randint(1, 100)
user_number = int(input("Enter a number: "))
difference = abs(number - user_number)
print("Generated number:", number)
print("Absolute difference:", difference)
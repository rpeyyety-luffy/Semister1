# Program to convert Fahrenheit to Celsius

# Take temperature input in Fahrenheit from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Formula to convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the converted temperature
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
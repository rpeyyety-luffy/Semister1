# Program to convert Celsius to Fahrenheit

# Take temperature input in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Formula to convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display the converted temperature
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

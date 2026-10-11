# Temperature Conversion Program

print("===================================")
print("     TEMPERATURE CONVERSION")
print("===================================")

# Get temperature from the user
temperature = float(input("Enter temperature value: "))

# Get the original unit
unit = input("Enter the original unit (C, F, or K): ").upper()

# Celsius
if unit == "C":
    fahrenheit = (temperature * 9 / 5) + 32
    kelvin = temperature + 273.15

    print("\nConverted Temperature:")
    print(f"Celsius:    {temperature:.2f} °C")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Kelvin:     {kelvin:.2f} K")

# Fahrenheit
elif unit == "F":
    celsius = (temperature - 32) * 5 / 9
    kelvin = (temperature - 32) * 5 / 9 + 273.15

    print("\nConverted Temperature:")
    print(f"Fahrenheit: {temperature:.2f} °F")
    print(f"Celsius:    {celsius:.2f} °C")
    print(f"Kelvin:     {kelvin:.2f} K")

# Kelvin
elif unit == "K":
    celsius = temperature - 273.15
    fahrenheit = (temperature - 273.15) * 9 / 5 + 32

    print("\nConverted Temperature:")
    print(f"Kelvin:     {temperature:.2f} K")
    print(f"Celsius:    {celsius:.2f} °C")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")

# Invalid input
else:
    print("\nInvalid unit!")
    print("Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

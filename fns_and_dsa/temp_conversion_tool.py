FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/59

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature_input = input("Enter the temperature you want to convert: ")
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

try:
    temperature_value = float(temperature_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numerical value.")

if scale == "C":
    result = convert_to_fahrenheit(temperature_value)
    print(f"{temperature_value} * C is equal to {result:2f}")
elif scale == "F":
    result = convert_to_celsius(temperature_value)
    print(f"{temperature_value} is equal to{result: 2f}")
else:
    print("Invalid temperatue. Please enter a numerical value.")
    


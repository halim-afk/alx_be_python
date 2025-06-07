FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temperature = int(input("Enter the temperature to convert: "))
type_of_teperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
def convert_to_celsius():
    fahrenheit = temperature
    celsius = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius} °C")

def convert_to_fahrenheit():
    celsius = temperature
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    print(f"{celsius} °C is {fahrenheit} °F")
    
if type_of_teperature == "C":
    convert_to_fahrenheit()
elif type_of_teperature == "F":
     convert_to_celsius()
else:
     print("Invalid temperature. Please enter a numeric value.")     
     
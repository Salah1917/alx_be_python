FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    temp_str = input("Enter the temperature to convert: ")
    
    try:
        temp = float(temp_str)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
   
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if type == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif type == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        print("Invalid temperature type. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
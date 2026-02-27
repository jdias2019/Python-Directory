def mode():
    print("=====================================")
    print("Temperature and Measurement Converter")
    print("=====================================")
    choice_mode = input("Temperature (1) or Measurement (2): ")

    if choice_mode == "1":
        print("=====================================")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        choice_temp = input("Enter your choice (1, 2 or 3): ")
        return choice_mode, choice_temp, None
    elif choice_mode == "2":
        print("1. Meters to Feet")
        print("2. Feet to Meters")
        choice_measure = input("Enter your choice (1 or 2): ")
        return choice_mode, None, choice_measure
    else:
        print("Invalid Option")
        return None, None, None


def temp(choice_temp):
    if choice_temp == "1":
        print("=====================================")
        c = float(input("Celsius: "))
        f = c * 9/5 + 32
        print("Fahrenheit:", f)
        print("=====================================")
    elif choice_temp == "2":
        print("=====================================")
        c = float(input("Celsius: "))
        k = c + 273.15
        print("Kelvin:", k)
        print("=====================================")
    elif choice_temp == "3":
        print("=====================================")
        f = float(input("Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Celsius:", c)
        print("=====================================")
    else:
        print("Invalid Option")


def measure(choice_measure):
    if choice_measure == "1":
        m = float(input("Meters: "))
        f = m * 3.28084
        print("Feet:", f)
        print("=====================================")
    elif choice_measure == "2":
        f = float(input("Feet: "))
        m = f * 0.3048
        print("Meters:", m)
        print("=====================================")

choice_mode, choice_temp, choice_measure = mode()

if choice_mode == "1" and choice_temp is not None:
    temp(choice_temp)
elif choice_mode == "2" and choice_measure is not None:
    measure(choice_measure)

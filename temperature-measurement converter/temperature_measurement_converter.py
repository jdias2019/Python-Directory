def mode():
    print("=====================================")
    print("Temperature and Measurement Converter")
    print("=====================================")
    choice_mode = input("Temperature (1) or Measurement (2): ")
    print("=====================================")
    if choice_mode == "1":
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        choice_temp = input("Enter your choice (1, 2 or 3): ")
    elif choice_mode == "2":
        print("1. Meters to Feet")
        print("2. Feet to Meters")
        choice_measure = input("Enter your choice (1 or 2): ")
    else:
        print("Invalid Optinon")

choice_mode = mode()
    




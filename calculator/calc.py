import math

def main():
    while True:
        num1 = float(input("1st Number: "))
        op = str(input("Operation (+, -, /, *, ^): "))
        num2 = float(input("2nd Number: "))

        if op == "+":
            print("Result =", num1 + num2)
        elif op == "-":
            print("Result =", num1 - num2)
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero.")
            else:
                print("Result =", num1 / num2)
        elif op == "*":
            print("Result =", num1 * num2)
        elif op == "^":
            print("Result =", pow(num1, num2))
        else:
            print("Enter a valid operation.")


if __name__ == "__main__":
    main()

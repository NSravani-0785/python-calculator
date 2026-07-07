from calculator import *
print("""
*************************************************
*                                               *
*        WELCOME TO PYTHON CALCULATOR           *
*                                               *
*            Version 1.0                        *
*************************************************
""")

history = []
memory = 0

def get_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid number.")

def show_menu():
    print("\n===== ENHANCED CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Modulus")
    print("9. Factorial")
    print("10. Memory Store")
    print("11. Memory Recall")
    print("12. Memory Clear")
    print("13. Show History")
    print("14. Exit")
    print("\n===== ======== =====")
while True:

    show_menu()

    choice = input("Enter Choice: ")

    if choice == "1":
        a = get_number("First Number: ")
        b = get_number("Second Number: ")
        result = add(a, b)
        print("Result =", result)
        history.append(f"{a}+{b}={result}")

    elif choice == "2":
        a = get_number("First Number: ")
        b = get_number("Second Number: ")
        result = subtract(a, b)
        print("Result =", result)
        history.append(f"{a}-{b}={result}")

    elif choice == "3":
        a = get_number("First Number: ")
        b = get_number("Second Number: ")
        result = multiply(a, b)
        print("Result =", result)
        history.append(f"{a}*{b}={result}")

    elif choice == "4":
        a = get_number("First Number: ")
        b = get_number("Second Number: ")
        result = divide(a, b)
        print("Result =", result)
        history.append(f"{a}/{b}={result}")

    elif choice == "5":
        a = get_number("Base: ")
        b = get_number("Exponent: ")
        result = power(a, b)
        print("Result =", result)
        history.append(f"{a}^{b}={result}")

    elif choice == "6":
        a = get_number("Enter Number: ")
        result = square_root(a)
        print("Result =", result)
        history.append(f"√{a}={result}")

    elif choice == "7":
        value = get_number("Value: ")
        percent = get_number("Percent: ")
        result = percentage(value, percent)
        print("Result =", result)
        history.append(f"{percent}% of {value}={result}")

    elif choice == "8":
        a = get_number("First Number: ")
        b = get_number("Second Number: ")
        result = modulus(a, b)
        print("Result =", result)
        history.append(f"{a}%{b}={result}")

    elif choice == "9":
        n = get_number("Enter Integer: ")
        result = factorial(n)
        print("Result =", result)
        history.append(f"{int(n)}!={result}")

    elif choice == "10":
        memory = get_number("Store Value: ")
        print("Memory Stored")

    elif choice == "11":
        print("Memory =", memory)

    elif choice == "12":
        memory = 0
        print("Memory Cleared")

    elif choice == "13":
        if history:
            print("\nHistory")
            for item in history:
                print(item)
        else:
            print("No history available.")

    elif choice == "14":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")

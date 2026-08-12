import math


def get_number(prompt):
    """Ensures the user inputs a valid numeric value."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def calculator():
    print("=" * 40)
    print("       ADVANCED CONSOLE CALCULATOR       ")
    print("=" * 40)

    while True:
        print("\nAvailable Operations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (√)")
        print("7. Sine (sin)")
        print("8. Cosine (cos)")
        print("9. Quit")

        choice = input("\nSelect an operation (1-9): ").strip()

        if choice == "9":
            print("\nGoodbye! Thanks for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("❌ Invalid choice! Please select a number between 1 and 9.")
            continue

        # Single-input operations
        if choice in ["6", "7", "8"]:
            num = get_number("Enter the number: ")

            if choice == "6":
                if num < 0:
                    print("❌ Error! Cannot calculate square root of a negative number.")
                else:
                    print(f"Result: √{num} = {math.sqrt(num)}")

            elif choice == "7":
                # Converts degrees to radians for math.sin
                print(f"Result: sin({num}°) = {math.sin(math.radians(num))}")

            elif choice == "8":
                # Converts degrees to radians for math.cos
                print(f"Result: cos({num}°) = {math.cos(math.radians(num))}")

        # Two-input operations
        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("❌ Error! Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif choice == "5":
                print(f"Result: {num1} ^ {num2} = {num1**num2}")

        print("-" * 40)


 
calculator()

class Calculator:

    def add(self, num1: float, num2: float) -> float:
        return num1 + num2

    def subtract(self, num1: float, num2: float) -> float:
        return num1 - num2

    def multiply(self, num1: float, num2: float) -> float:
        return num1 * num2

    def divide(self, num1: float, num2: float):
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2


def get_number(prompt_text: str) -> float:
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Error: Invalid input. Please enter a valid number, not letters.")


def main():
    calc = Calculator()

    while True:
        print("\n--- Calculator App Menu ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ").strip()

        if choice == '5':
            print("Exiting Calculator App. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                result = round(num1 + num2,3)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = round(num1 - num2,3)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = round(num1 * num2,3)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

    #round the float for 1,2,3
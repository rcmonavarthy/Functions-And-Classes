import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


def main():
    while True:
        print("\n--- Area Calculator Menu ---")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Exit")

        choice = input("Choose which area to calculate (1-3): ").strip()

        if choice == '3':
            print("Exiting program.")
            break

        if choice == '1':
            try:
                radius = float(input("Enter the radius of the circle: "))
                if radius < 0:
                    print("Error: Radius cannot be negative.")
                    continue
                circle = Circle(radius)
                print(f"Area of the circle: {circle.calculate_area():.2f}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '2':
            try:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                if length < 0 or width < 0:
                    print("Error: Dimensions cannot be negative.")
                    continue
                rectangle = Rectangle(length, width)
                print(f"Area of the rectangle: {rectangle.calculate_area():.2f}")
            except ValueError:
                print("Error: Please enter a valid number.")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
def sum_numbers(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return n + sum_numbers(n - 1)


def factorial(n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)


def power(base, exponent):
    # Base case
    if exponent == 0:
        return 1

    # Recursive case
    return base * power(base, exponent - 1)


def main():
    choice = ""

    while choice != "q":
        print("=== RECURSIVE NUMBER EXPLORER ===")
        print("1. Sum of Natural Numbers")
        print("2. Factorial Calculator")
        print("3. Power Calculator")
        print("q. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a nonnegative integer: "))
            print("Sum of natural numbers:", sum_numbers(number))

        elif choice == "2":
            number = int(input("Enter a nonnegative integer: "))
            print("Factorial:", factorial(number))

        elif choice == "3":
            base = int(input("Enter the base: "))
            exponent = int(input("Enter a nonnegative integer exponent: "))
            print("Power:", power(base, exponent))

        elif choice == "q":
            print("Thank you for using Recursive Number Explorer!")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

def calculate_average(a, b, c):
    return (a + b + c) / 3


def find_highest(a, b, c):
    return max(a, b, c)

def find_lowest(a, b, c):
    return min(a, b, c)

def check_pass(score):
    return score >= 60


def display_result(name, average):
    print(f"{name}'s average score is {average:.2f}.")

def read_score(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_three_scores():
    return (
        read_score("Enter the first test score: "),
        read_score("Enter the second test score: "),
        read_score("Enter the third test score: "),
    )


def display_menu():
    print("\n== Student Grade Management ==")
    print("1. Calculate Average")
    print("2. Find Highest Score")
    print("3. Find Lowest Score")
    print("4. Check Pass or Fail")
    print("5. Display Student Result")
    print("6. Quit")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            scores = read_three_scores()
            print(f"Average score: {calculate_average(*scores):.2f}")
        elif choice == "2":
            scores = read_three_scores()
            print(f"Highest score: {find_highest(*scores):g}")
        elif choice == "3":
            scores = read_three_scores()
            print(f"Lowest score: {find_lowest(*scores):g}")
        elif choice == "4":
            average = read_score("Enter the average score: ")
            result = "Pass" if check_pass(average) else "Fail"
            print(f"Result: {result}")
        elif choice == "5":
            name = input("Enter the student's name: ").strip()
            average = read_score("Enter the average score: ")
            display_result(name, average)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
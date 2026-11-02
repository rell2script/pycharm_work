
def rental_car():
    car = input("What kind of rental car would you like? ")
    print(f"Let me see if I can find you a {car}.")


def restaurant_seating():
    people = int(input("How many people are in your dinner group? "))
    if people > 8:
        print("You'll have to wait for a table.")
    else:
        print("Your table is ready.")


def multiples_of_ten():
    number = int(input("Enter a number: "))
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
    else:
        print(f"{number} is not a multiple of 10.")


def pizza_toppings():
    while True:
        topping = input("Enter a pizza topping (or 'quit' to finish): ")
        if topping.lower() == "quit":
            break
        print(f"I'll add {topping} to your pizza.")


def three_exits():
    print("a) Conditional test in the while statement")
    topping = input("Enter a topping (or 'quit'): ")
    while topping.lower() != "quit":
        print(f"I'll add {topping} to your pizza.")
        topping = input("Enter another topping (or 'quit'): ")

    print("\nb) Active variable")
    active = True
    while active:
        topping = input("Enter a topping (or 'quit'): ")
        if topping.lower() == "quit":
            active = False
        else:
            print(f"I'll add {topping} to your pizza.")

    print("\nc) break statement")
    while True:
        topping = input("Enter a topping (or 'quit'): ")
        if topping.lower() == "quit":
            break
        print(f"I'll add {topping} to your pizza.")


def deli():
    sandwich_orders = ["tuna", "turkey", "veggie", "pastrami"]
    finished_sandwiches = []
    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)
    print("Finished sandwiches:", ", ".join(finished_sandwiches))


def dream_vacation():
    responses = {}
    while True:
        name = input("What is your name? (or 'quit' to finish): ")
        if name.lower() == "quit":
            break
        place = input("If you could visit one place in the world, where would you go? ")
        responses[name] = place
    print("\nDream vacation poll results:")
    for name, place in responses.items():
        print(f"{name} would like to visit {place}.")


def weekly_expenses():
    import matplotlib.pyplot as plt

    expenses = {}
    for category in ("Food", "Transportation", "Entertainment"):
        expenses[category] = float(input(f"How much do you spend on {category} in a week? $"))
    plt.pie(expenses.values(), labels=expenses.keys(), autopct="%1.1f%%")
    plt.title("Weekly Expenses")
    plt.axis("equal")
    plt.show()


def study_hours_tracker():
    import matplotlib.pyplot as plt

    study_hours = {}
    for subject in ("Python", "Math", "Science"):
        study_hours[subject] = int(input(f"How many hours did you study {subject}? "))
    plt.bar(study_hours.keys(), study_hours.values())
    plt.title("Study Hours by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Hours Studied")
    plt.show()


def temperature_tracker():
    temperatures = []
    while True:
        temperatures.append(float(input("Enter a temperature: ")))
        again = input("Would you like to enter another temperature? (yes/no): ")
        if again.strip().lower() not in ("yes", "y"):
            break
    print("Temperatures:", temperatures)
    print("Highest temperature:", max(temperatures))
    print("Lowest temperature:", min(temperatures))


def student_grades():
    grades = {}
    while True:
        name = input("Enter a student's name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        grades[name] = float(input(f"Enter {name}'s grade: "))
        if input("Add another student? (yes/no): ").strip().lower() not in ("yes", "y"):
            break
    if not grades:
        print("No grades were entered.")
        return
    print("\nStudent grades:")
    for name, grade in grades.items():
        print(f"{name}: {grade:g}")
    print(f"Average grade: {sum(grades.values()) / len(grades):.2f}")


def favorite_foods():
    foods = []
    while True:
        foods.append(input("Enter a favorite food: ").strip())
        if input("Add another food? (yes/no): ").strip().lower() not in ("yes", "y"):
            break
    print("Your favorite foods:", foods)
    search_food = input("Enter a food to search for: ").strip()
    if search_food.lower() in (food.lower() for food in foods):
        print(f"{search_food} is in your list.")
    else:
        print(f"{search_food} is not in your list.")


def store_inventory():
    inventory = {}
    while True:
        product = input("Enter a product name: ").strip()
        quantity = int(input(f"How many units of {product} are available? "))
        inventory[product] = quantity
        if input("Add another product? (yes/no): ").strip().lower() not in ("yes", "y"):
            break
    print("\nInventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")
    print("Total units:", sum(inventory.values()))


def shopping_list():
    items = []
    prices = []
    while True:
        item = input("Enter an item to purchase: ").strip()
        price = float(input(f"Enter the price of {item}: $"))
        items.append(item)
        prices.append(price)
        if input("Add another item? (yes/no): ").strip().lower() not in ("yes", "y"):
            break
    total = sum(prices)
    print("\nShopping list:")
    for item, price in zip(items, prices):
        print(f"{item}: ${price:.2f}")
    print(f"Total cost: ${total:.2f}")
    budget = float(input("Enter your budget: $"))
    difference = budget - total
    if difference >= 0:
        print(f"Money remaining: ${difference:.2f}")
    else:
        print(f"You are over budget by ${-difference:.2f}.")


def movie_ratings():
    movies = []
    ratings = []
    while True:
        movie = input("Enter a movie title: ").strip()
        rating = int(input(f"Rate {movie} from 1 to 5: "))
        while rating < 1 or rating > 5:
            rating = int(input("Please enter a rating from 1 to 5: "))
        movies.append(movie)
        ratings.append(rating)
        if input("Enter another movie? (yes/no): ").strip().lower() not in ("yes", "y"):
            break
    print("\nMovie ratings:")
    for movie, rating in zip(movies, ratings):
        print(f"{movie}: {rating}/5")
    print("Highest rating:", max(ratings))


EXERCISES = {
    1: rental_car,
    2: restaurant_seating,
    3: multiples_of_ten,
    4: pizza_toppings,
    5: three_exits,
    6: deli,
    7: dream_vacation,
    8: weekly_expenses,
    9: study_hours_tracker,
    10: temperature_tracker,
    11: student_grades,
    12: favorite_foods,
    13: store_inventory,
    14: shopping_list,
    15: movie_ratings,
}


def main():
    print("Python Exercises 1–16")
    print("Choose a number from 1 to 15, or 0 to quit.")
    while True:
        choice = input("Exercise: ").strip()
        if choice == "0":
            break
        try:
            exercise_number = int(choice)
        except ValueError:
            print("Please enter a number from 0 to 16.")
            continue
        exercise = EXERCISES.get(exercise_number)
        if exercise is None:
            print("Please enter a number from 0 to 16.")
            continue
        try:
            exercise()
        except KeyboardInterrupt:
            print("\nExercise stopped.")


if __name__ == "__main__":
    main()
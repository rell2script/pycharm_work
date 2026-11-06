def calculate_grade(score):
    """Return the letter grade for a score from 0 to 100."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def calculate_bill(item_name, price, quantity, discount=0.05):
    """Return (item name, final amount), applying the applicable discount."""
    total = price * quantity
    if total > 100:
        discount = 0.10
    return item_name, total * (1 - discount)


def show_bill(result):
    item_name, amount = result
    print(f"{item_name}: ${amount:.2f}")


if __name__ == "__main__":
    # Positional arguments
    show_bill(calculate_bill("Notebook", 4.50, 3))
    # Keyword arguments
    show_bill(calculate_bill(item_name="Headphones", price=35, quantity=2))
    # Positional and keyword arguments
    show_bill(calculate_bill("Desk", 60, quantity=2))
def calculate_average(*temperatures):

  """Return the average of any number of temperatures."""

  if not temperatures:

    raise ValueError("At least one temperature is required.")

  return sum(temperatures) / len(temperatures)





def read_temperature(day):

  while True:

    try:

      return float(input(f"Enter the temperature for day {day}: "))

    except ValueError:

      print("Please enter a valid number.")





def main():

  temperatures = []

  day = 1

  while day <= 7:

    temperatures.append(read_temperature(day))

    day += 1



  average = calculate_average(*temperatures)

  if average > 80:

    classification = "Hot week"

  elif average >= 60:

    classification = "Moderate week"

  else:

    classification = "Cold week"



  print(f"Average temperature: {average:.2f}")

  print(classification)





if __name__ == "__main__":

  main()



def update_balance(balance, amount, transaction="deposit"):

  """Return the balance after a deposit or permitted withdrawal."""

  if transaction == "deposit":

    return balance + amount

  if transaction == "withdraw":

    if amount > balance:

      print("Withdrawal denied: insufficient funds.")

      return balance

    return balance - amount

  raise ValueError("Transaction must be 'deposit' or 'withdraw'.")



def read_amount():

  while True:

    try:

      amount = float(input("Enter amount: $"))

      if amount < 0:

        print("Amount cannot be negative.")

        continue

      return amount

    except ValueError:

      print("Please enter a valid number.")

def main():

  balance = 0.0

  while True:

    print("\n===== Bank Account Manager =====")

    print("1. Deposit")

    print("2. Withdraw")

    print("3. Check Balance")

    print("4. Exit")

    choice = input("Select an option (1-4): ").strip()



    if choice == "1":

      balance = update_balance(balance, read_amount(), "deposit")

      print(f"Current balance: ${balance:.2f}")

    elif choice == "2":

      balance = update_balance(balance, read_amount(), "withdraw")

      print(f"Current balance: ${balance:.2f}")

    elif choice == "3":

      print(f"Current balance: ${balance:.2f}")

    elif choice == "4":

      print("Goodbye!")

      break

    else:

      print("Invalid option. Please select a number from 1 to 4.")



if __name__ == "__main__":

  main()






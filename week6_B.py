ages = [4, 10, 16, 25, 70]
for age in ages:
    if age <= 5:
        price = 0
    elif age <= 12:
        price = 8
    elif age <= 17:
        price = 10
    elif age <= 64:
        price = 15
    else:
        price = 10
    print(f"Age: {age}, Ticket price: ${price}")
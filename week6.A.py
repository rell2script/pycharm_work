#1
order={"drink":"Latte","size":"Large","price":5.50,"quantity":2}
#2
print(order["drink"],order["price"])
#3
for key in order.keys(): print(key)
#4
for value in order.values():print(value)
#5
for key in order:
    print(f"{key}: {order[key]}")
#6
order = {"drink": "Latte","size": "Large","quantity": 2,}
#7,8,9
order["drink"] = "Iced Coffee"
order["size"] = "Medium"
order["whipped_cream"] = "Yes"
order["flavor"] = "Vanilla"
#10Indexing a missing key raises a keyError
#print(order["milk"])
#11
print(order.get("milk"))
#12
order["flavor"] = "Caramel"
order["quantity"] = 3
#13
order["pickup"] = "10:30 AM"
#14
print("final order:")
for key in order:
    print(order[key])
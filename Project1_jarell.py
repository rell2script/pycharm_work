# Shopper 1
shopper_name = "Jarell Noble"

grocery_1_price = 1.32
grocery_2_price = 6.35
grocery_3_price = 2.75
grocery_4_price = 4.50
grocery_5_price = 5.25

grocery_1_quantity = 6
grocery_2_quantity = 2
grocery_3_quantity = 3
grocery_4_quantity = 1
grocery_5_quantity = 2

total_bill = (grocery_1_price * grocery_1_quantity
              + grocery_2_price * grocery_2_quantity
              + grocery_3_price * grocery_3_quantity
              + grocery_4_price * grocery_4_quantity
              + grocery_5_price * grocery_5_quantity)

total_items = (grocery_1_quantity
    + grocery_2_quantity
    + grocery_3_quantity
    + grocery_4_quantity
    + grocery_5_quantity)

average_price = round(total_bill / total_items,2)

print(f"{shopper_name.title()}: Total bill ${total_bill}, average price per item ${average_price}")

# Shopper 2
shopper_name = "Cindy James"

grocery_1_price = 8.50
grocery_2_price = 1.75
grocery_3_price = 4.53
grocery_4_price = 3.50
grocery_5_price = 6.25

grocery_1_quantity = 3
grocery_2_quantity = 5
grocery_3_quantity = 2
grocery_4_quantity = 4
grocery_5_quantity = 1

total_bill = ( grocery_1_price * grocery_1_quantity
    + grocery_2_price * grocery_2_quantity
    + grocery_3_price * grocery_3_quantity
    + grocery_4_price * grocery_4_quantity
    + grocery_5_price * grocery_5_quantity
)

total_items = (grocery_1_quantity
    + grocery_2_quantity
    + grocery_3_quantity
    + grocery_4_quantity
    + grocery_5_quantity
)

average_price = round(total_bill / total_items,2)

print(f"{shopper_name.title()}: Total bill ${total_bill}, average price per item ${average_price}")


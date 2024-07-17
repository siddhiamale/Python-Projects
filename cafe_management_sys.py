# Cafe Management System
#define menu of restaurant
menu = {
    'Pizza' : 50,
    'Pasta' : 40,
    'Burger': 50,
    'Salad' : 30,
    'Coffee' : 40
}

#Greet
print("Welcome to FOODIES CAFE....")
print("Pizza : Rs50\nPasta : Rs40\nBurger : Rs50\nSalad : Rs30\nCoffee : Rs40")

#ordering
order_total = 0

item_1 = input("Enter the item you want to order...:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order list...")
else:
    print(f"Ordered item {item_1} is not available yet..!") 

another_order = input("Do you want to add another item (yes/no):")
if another_order == "yes":
    item_2 = input("Enter the second item you want to add in your order list: ")

    if item_2 in menu:
        order_total += menu[item_2]   
        print(f"Your second item {item_2} has been added to your order list...")
    else:
        print(f"Ordered item {item_2} is not available yet..!") 


#printing total
 
print(f"The total amount of items is {order_total}")  
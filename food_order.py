menu = {
    "pizza" :500000,
    "pasta":200000,
    "macaroni":120000,
    "Risotto":7000000
}
print("Italian food menu:")
for food,price in menu.items():
    print(f"{food}: {price} Toman")
order = {}
while True:
    food_name = input("Enter the food name (type 'done' to finish):")
    if food_name.lower()=="done":
        break
    if food_name not in menu:
        print("This food is not available in the menu. Please enter another food.")
        continue
    quantity = int(input("Enter the quantity:"))
    if food_name in order:
        order[food_name] += quantity
    else:
        order[food_name] = quantity
total_price = 0
for food , quantity in order.items():
    total_price += menu[food]*quantity
print(f"Your total price is: {total_price} Toman")
choice = input("Type 'pay' to pay or 'cancel' to cancel the order: ")
if choice.lower() == "pay":
    print("Processing payment, please wait...")
    input("Press Enter to continue...")
    print("Your order is ready for pickup at one of the store counters.")
else:
    print("Your order has been cancelled.")

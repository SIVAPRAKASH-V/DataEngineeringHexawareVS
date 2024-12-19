inventory = {
    "Apple" : [5, 100.0],"Orange": [6,70.5],"Grapes": [10, 90.5]
}
def display(inventory):
    print("Stock details")
    for key,value in inventory.items():
        qty,cost=value
        print("{} has {} kgs and cost {} per kg.".format(key,qty,cost))

def sell(inventory):
    product_name = input("Enter the product name: ")
    if product_name in inventory:
        quantity, price = inventory[product_name]
        units_to_buy = int(input("Enter the quantity to buy: "))
        if units_to_buy <= quantity:
            inventory[product_name][0] -= units_to_buy
            total_cost = units_to_buy * price
            print("Total cost: ₹{}".format(total_cost))
        else:
            print("Not enough quantity available.")
    else:
        print("Product not found.")   
def restock(inventory):
    product_name = input("Enter the product name to restock: ")
    if product_name in inventory:
        quantity = int(input("Enter the quantity to add: "))
        inventory[product_name][0] += quantity
        print("Inventory restocked.")
    else:
        print("Product not found.")
while True:
    choice = input("1. Display\n2. Sell\n3. Restock\n4. Exit\nEnter choice")
    if choice=='1':
        display(inventory)
    elif choice=='2':
        sell(inventory)
    elif choice =='3':
        restock(inventory)
    else:
        break













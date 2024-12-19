customers = {}
product_catalog = {
    "Laptop": {"price": 75000, "stock": 10},
    "Smartphone": {"price": 30000, "stock": 20},
    "Headphones": {"price": 2000, "stock": 50},
    "Camera": {"price": 40000, "stock": 5}
}
order_history = {}

def add_customer():
    c_id = int(input("Enter Customer id: "))
    c_name = input("Enter Customer Name: ")
    c_address = input("Enter Address: ")
    c_phone = int(input("Enter Phone No.: "))

    customers['customer_id'] = c_id
    customers['Name']= c_name
    customers['Address']=c_address
    customers['Phone']=c_phone

def place_order(customer_id, **kwargs):
    if customer_id not in customers:
        print("Customer not found. Please add the customer first.")
        return

    print("\nAvailable products:")
    for product, details in product_catalog.items():
        print(f"{product} - Price: {details['price']}, Stock: {details['stock']}")
    
    order = []
    total_cost = 0
    
    while True:
        product_name = input("Enter the product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        if product_name not in product_catalog:
            print("Product not available. Please choose from the catalog.")
            continue
        
        quantity = int(input(f"Enter the quantity of {product_name}: "))
        
        if product_catalog[product_name]["stock"] < quantity:
            print(f"Sorry, only {product_catalog[product_name]['stock']} units available.")
            continue
        
        product_price = product_catalog[product_name]["price"]
        product_catalog[product_name]["stock"] -= quantity
        order.append({"product": product_name, "quantity": quantity, "price": product_price})
        total_cost += product_price * quantity
    
    # Process any additional kwargs (promo codes, delivery options)
    promo_code = kwargs.get("promo_code", None)
    delivery_preference = kwargs.get("delivery_preference", "Standard Delivery")
    
    # Apply promo code if available
    discount = 0
    if promo_code == "SAVE10":
        discount = total_cost * 0.1
        total_cost -= discount
        print(f"Promo applied! You saved ₹{discount:.2f}")
    
    # Store the order in order history
    order_history[customer_id] = order
    
    # Generate invoice
    generate_invoice(customer_id, total_cost, discount, delivery_preference)

# Function to generate an invoice
def generate_invoice(customer_id, total_cost, discount, delivery_preference, *args):
    print("\n--- Invoice ---")
    print(f"Customer: {customers[customer_id]['name']}")
    print(f"Delivery Preference: {delivery_preference}")
    
    print("\nItems ordered:")
    for item in order_history[customer_id]:
        print(f"{item['product']} - Quantity: {item['quantity']} - Price per unit: ₹{item['price']}")
    
    # Apply additional costs (taxes, shipping fees)
    shipping_fee = 50
    tax = total_cost * 0.05
    final_total = total_cost + tax + shipping_fee
    
    # Display summary
    print(f"\nTotal Cost: ₹{total_cost:.2f}")
    print(f"Discount Applied: ₹{discount:.2f}")
    print(f"Tax (5%): ₹{tax:.2f}")
    print(f"Shipping Fee: ₹{shipping_fee}")
    print(f"Final Total: ₹{final_total:.2f}")




def show_order_history(customer_id):
    if customer_id in order_history:
        print(f"\nOrder history for {customers[customer_id]['name']}:")
        for item in order_history[customer_id]:
            print(f"{item['quantity']} x {item['product']} @ ₹{item['price']} each")
    else:
        print("No orders found for this customer.")


while True:
    print("\nE-commerce Order Management System")
    print("1. Add Customer")
    print("2. Place Order")
    print("3. Show Order History")
    print("4. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == '1':
        add_customer()
    elif choice == '2':
        customer_id = input("Enter customer ID to place an order: ")
        promo = input("Enter promo code (if any): ")
        delivery = input("Enter delivery preference (Standard/Express): ")
        place_order(customer_id, promo_code=promo, delivery_preference=delivery)
    elif choice == '3':
        customer_id = input("Enter customer ID to view order history: ")
        show_order_history(customer_id)
    elif choice == '4':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")







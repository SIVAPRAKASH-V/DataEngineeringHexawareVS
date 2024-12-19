class FoodItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self):
        return self.stock > 0

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise Exception('Not enough stock for {}'.format(self.name))
        self.stock -= quantity

    def __str__(self):
        return '{}: ${}, Available: {}.'.format(self.name,self.price,self.stock)
#######################################################################################

class Coupon:
    def __init__(self, code, discount_percentage, is_valid=True):
        self.code = code
        self.discount_percentage = discount_percentage
        self.is_valid = is_valid

    def apply_discount(self, total_amount):
        if not self.is_valid:
            raise Exception('Coupon {} is expired or invalid.'.format(self.code))

        return total_amount * (1 - self.discount_percentage / 100)

    def __str__(self):
        # return f"Coupon {self.code}: {self.discount_percentage}% discount"
        return 'Coupon {}: {}% discount.'.format(self.code,self.discount_percentage)

###################################################################################


class Order:
    def __init__(self):
        self.items = []
        self.coupon = None

    def add_item(self, food_item, quantity):
        if not food_item.is_available():
            # raise Exception(f"Item {food_item.name} is out of stock.")
            raise Exception('Item {} is out of stock.'.format(food_item.name))

        food_item.reduce_stock(quantity)
        self.items.append((food_item, quantity))

    def apply_coupon(self, coupon):
        if not coupon.is_valid:
            # raise Exception(f"Invalid coupon code {coupon.code}")
            raise Exception('Invalid coupon code {}'.format(coupon.code))
        self.coupon = coupon

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items)
        if self.coupon:
            total = self.coupon.apply_discount(total)
        return total

    def __str__(self):
        return f"Order contains: {', '.join([item.name for item, _ in self.items])}"


###########################################################


class Payment:
    def pay(self, amount):
        raise NotImplementedError("This method should be overridden by subclasses.")

###########################################################

class CreditCardPayment(Payment):
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance in credit card.")
        self.balance -= amount
        # print(f"Paid {amount} using Credit Card. Remaining balance: {self.balance}")
        print("Paid {} using Credit Card. Remaining balance: {}".format(amount,self.balance))


#############################################################

class WalletPayment(Payment):
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance in wallet.")
        self.balance -= amount
        # print(f"Paid {amount} using Wallet. Remaining balance: {self.balance}")
        print("Paid {} using Wallet. Remaining balance: {}".format(amount,self.balance))


########################################################################


import datetime

def log_order(order, total_amount):
    with open("order_log.txt", "a") as f:
        # log_message = f"{datetime.datetime.now()}: Order - {order}. Total: ${total_amount}\n"
        log_message = '{}: Order - {}. Total: ${}\n'.format(datetime.datetime.now(),order,total_amount)

        f.write(log_message)



###################################################################################




def main():
    # Available Food Items (sample items for demo purposes)
    menu = [
        FoodItem("Pizza", 10, 5),
        FoodItem("Burger", 8, 3),
        FoodItem("Fries", 5, 2),
        FoodItem("Pasta", 12, 4)
    ]

    # Available Coupons (sample coupons)
    coupons = {
        "SAVE10": Coupon("SAVE10", 10, is_valid=True),
        "DISCOUNT20": Coupon("DISCOUNT20", 20, is_valid=True),
        "EXPIRED20": Coupon("EXPIRED20", 20, is_valid=False)
    }

    # Create an order
    order = Order()

    print("Welcome to the Online Food Ordering System")
    print("Available Food Items:")
    for idx, item in enumerate(menu, 1):
        # print(f"{idx}. {item.name} - ${item.price} (Stock: {item.stock})")
        print('{}. {} - ${} (Available: {})'.format(idx,item.name,item.price,item.stock))


    while True:
        try:
            # User selects food items and quantity
            food_choice = int(input("Enter the food item you want to add (or 0 to finish): ")) - 1
            if food_choice == -1:
                break

            if food_choice < 0 or food_choice >= len(menu):
                print("Invalid food selection. Try again.")
                continue

            # quantity = int(input(f"Enter quantity for {menu[food_choice].name}: "))
            quantity = int(input('Enter quantity for {}: '.format(menu[food_choice].name)))

            order.add_item(menu[food_choice], quantity)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            # print(f"Error: {e}")
            print('Error: {}'.format(e))


    # Ask if user has a coupon code
    coupon_code = input("Enter coupon code (press Enter to skip): ").strip()
    if coupon_code:
        coupon = coupons.get(coupon_code)
        try:
            if coupon:
                order.apply_coupon(coupon)
                print(f"Coupon {coupon_code} applied.")
            else:
                print("Invalid coupon code.")
        except Exception as e:
            print(f"Error: {e}")

    # Display total amount
    try:
        total = order.calculate_total()
        print(f"Total amount to be paid after applying coupon (if any): ${total:.2f}")
    except Exception as e:
        print(f"Error calculating total: {e}")
        return

    # Payment section
    print("Select payment method:")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. Wallet")

    payment_choice = input("Enter payment method (1/2/3): ").strip()

    try:
        if payment_choice == '1':
            balance = float(input("Enter your credit card balance: "))
            payment_method = CreditCardPayment(balance)
        elif payment_choice == '2':
            balance = float(input("Enter your debit card balance: "))
            payment_method = DebitCardPayment(balance)
        elif payment_choice == '3':
            balance = float(input("Enter your wallet balance: "))
            payment_method = WalletPayment(balance)
        else:
            print("Invalid payment method selection.")
            return

        # Try to pay the amount
        payment_method.pay(total)

        # Log the order after successful payment
        log_order(order, total)
        print("Order completed successfully. Thank you for your purchase!")

    except ValueError:
        print("Invalid input for payment. Please enter a valid number.")
    except Exception as e:
        print(f"Payment Error: {e}")


if __name__ == "__main__":
    main()

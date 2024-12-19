
###########################################%%%%%%%%%%%%%%%%%%
# class OutOfStockError(Exception):
#     pass

def apply_coupon(cart, coupon_code):
    if coupon_code == "INVALID":
        raise ValueError("Invalid coupon code!")
    else:
        print("Coupon applied successfully")

# def checkout(cart, stock):
#     if cart > stock:
#         raise OutOfStockError("Not enough stock available!")
#     else:
#         print("Checkout successful")

try:
    apply_coupon(["item1"], "INVALID")
except ValueError as e:
    print(e)

# try:
#     checkout(5, 2)
# except OutOfStockError as e:
#     print(e)
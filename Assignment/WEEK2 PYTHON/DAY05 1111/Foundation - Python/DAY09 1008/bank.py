curr_balance = 500
while True:
    choice = input("1. View balance\n2. Deosit\n3. withdraw\n4. Exit\nEnter choice")
    if choice=='1':
        print(curr_balance)
    elif choice=='2':
        amt = int(input("Enter Amount to deposit: "))
        curr_balance += amt
        print("Amount Deposited successfully..")
    elif choice =='3':
        amt = int(input("Enter Amount to withdraw: "))
        if amt>curr_balance:
            print("Insufficient Balance..")
        else:
            curr_balance= curr_balance - amt
            print("Amount Withdrawn successfully..")
    else:
        break

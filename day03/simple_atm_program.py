# Simple ATM

# Display a menu
# choose from menu
# if depodit then depodited amouunt plus starting amount
# if withdrawal the starting amount minus withdrwal amount
# if check balance display starting amount
# if exit end the program

starting_amount = 1000


menu = ["Balance", "Deposit", "Withdraw", "Exit"]

while True:
    print("## Choose from the list below: ##")
    for i, menu_list in enumerate(menu, 1):
        print(f"{i}. {menu_list}")

    user = int(input("Eneter a number: "))

    if user == 2:
        deposit = float(input("Enter the amount you want to deposit: "))
        Starting_amount = deposit + starting_amount
        print(Starting_amount)

    elif user == 3:
        withdrawal = float("Enter amout you what to withdraw: ")
        
        if withdrawal > starting_amount:
            print("Insufficient funds.")
        else:
            starting_amount = starting_amount - withdrawal
            print("Please collect your cash of {starting_amount}")
    elif user == 1:
        print("Your balnce is: {starting_amount}")

    elif user == 4:
        print("Thank you for using our bank!!")
        break
    else:
        print("Please try again")
    









import csv
from datetime import date
from expenses import Expenses

# Expense Tracker
# ask user to enter their expense and print them
# save user expenses to a csv file
# read a file and give the sammarie of the expenses

def expenses_budget():

    print("##...User expenses...##")

    user_date = date.today()

    user_expense_name = input("Enter the name of your expense: ")
    amount_of_expense = float(input("Enter the amout of your expense: "))
    print(f"{user_expense_name}: R{amount_of_expense}")

    expense_category = ["Food",
                        "Home",
                        "Work",
                        "Entertainment"]
    
    while True:
        print("##..Select the category of your expense..##")

        for i, name in enumerate(expense_category):
            print(f'{i + 1}. {name}')

        choice = f"[1 - {len(expense_category)}]"
        user_choice = int(input(f"Choose from {choice}: ")) - 1

        if user_choice in range(len(expense_category)):
            selected_index = expense_category[user_choice]
            new_expense = Expenses(date = user_date, name = user_expense_name, category = selected_index, amount = amount_of_expense)
            return new_expense
        else:
            print("Invalid value, Please try again!!.")

        


def main():
     
    expense = expenses_budget()
    print(expense)

if __name__ == "__main__":
    main()


  


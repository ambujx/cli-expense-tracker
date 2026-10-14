import json
import string
import os
import subprocess
from ui import section_heading
import time


def clear_terminal():
    # Select the terminal-clearing command for the operating system.
    command = 'clear' if os.name == 'nt' else 'clear'

    # Execute securely using the subprocess module
    subprocess.run(command, shell=True)


def load_json():
    if not os.path.exists("expenses.json"):
        return []

    with open("expenses.json", "r") as file:
        try:
            return json.load(file)
        except:
            return []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_json()

categories = []

for item in expenses:
    category = item['category']
    if category not in categories:
        categories.append(category)


def show_menu():
    print()
    section_heading('MAIN MENU')
    print("1 -> Add Expense")
    print("2 -> View Expenses")
    print("3 -> Delete Expense")
    print("4 -> Exit")


def write_expense_name():
    while True:
        expName = input('\tExpense name: ')
        if expName == "0":
            return 0
        try:
            expName = float(expName)
            typecheck = False
        except ValueError:
            typecheck = True
        if(expName == ""):
            print("This field cannot be empty. Please try again.")
            continue
        elif (typecheck == True):
            return expName
        elif(typecheck == False):
            print('Please enter a valid expense name.')


def write_expense_amount():
    while True:
        while True:
            try:
                expAmount = float(input('\tAmount: '))
                break
            except ValueError:
                print('Please enter a valid numeric amount.')
        if expAmount == 0:
            return 0
        elif expAmount > 0 and expAmount < 9999999999:
            return expAmount
        elif expAmount == 'inf':
            print("The amount must be finite.")
        else:
            print('The amount must be greater than zero and finite. Please try again.')


def choose_category():

    if not categories:
        categoryOption = 1

    else:
        section_heading("CHOOSE CATEGORY")
        for index, category in enumerate(categories, start=1):
            print(f"{index}-> {category}")
        print(f"{len(categories)+1}-> Create new category")
        while True:
            while True:
                try:
                    categoryOption = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Please enter a whole number.")

            if categoryOption == 0:
                expCategory = 0
                return expCategory

            if categoryOption >= 1 and categoryOption <= len(categories)+1:
                break
            else:
                print("Invalid option. Please choose an option from the list.")

    if categoryOption == len(categories)+1:
        while True:
            print("0 -> Back")
            expCategory = input('\tNew category name: ')
            if expCategory == "0":
                return 0
            expCategory = string.capwords(expCategory)
            try:
                float(expCategory)
                typecheck = False
            except ValueError:
                typecheck = True
            if typecheck == False:
                print('Please enter a valid expense name.')
                continue
            elif(expCategory == ""):
                print("This field cannot be empty. Please try again.")
                continue
            elif expCategory in categories:
                print(f"Category already present at: {categories.index(expCategory)+1}")
            else:
                categories.append(expCategory)
                break

    elif categoryOption >= 1 and categoryOption <= len(categories):
        expCategory = categories[categoryOption-1]
    return expCategory


def add_expense():
    while True:
        clear_terminal()
        section_heading("ADD EXPENSE")

        print("0 -> Back")
        expName = write_expense_name()
        if expName == 0:
            break

        expAmount = write_expense_amount()
        if expAmount == 0:
            break

        expCategory = choose_category()
        if expCategory == 0:
            break

        expense_dict = {
            'name': expName,
            'amount': expAmount,
            'category': expCategory
        }

        expenses.append(expense_dict)

        save_expenses()

        clear_terminal()
        print('Expense added successfully.')
        break


def show_expense_view():
    print("1 -> View All")
    print("2 -> View By Category")
    print("3 -> Back")


def view_all_expenses():
    clear_terminal()
    totalAmount = 0
    section_heading("ALL EXPENSES")
    print(f"\n{'No.':<5}{'Expense':<15}{'Amount':<12}{'Category'}")

    for index, expense in enumerate(expenses, start=1):
        print(f"\n{index:<5} {expense['name']:<15} {expense['amount']:<12} {expense['category']}")
        totalAmount += expense['amount']
    print(f"\nTotal: {totalAmount}\n")


def view_by_category():
    clear_terminal()
    section_heading("CHOOSE CATEGORY TO VIEW")
    for index, category in enumerate(categories, start=1):
        print(f"{index} -> {category}", end=" ")
        totalAmount = 0
        for expense in expenses:
            if expense['category'] == category:
                totalAmount += expense['amount']
        print(totalAmount)

    while True:
        while True:
            try:
                chooseCat = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Invalid Input, Enter only integers")
        if chooseCat >= 1 and chooseCat <= len(categories):
            break
        else:
            print("Invalid option. Please choose an option from the list.")

    target_category = categories[chooseCat-1]
    clear_terminal()
    section_heading(f"EXPENSES FROM '{target_category}'")
    index = 0
    total = 0
    for expense in expenses:
        if expense['category'] == target_category:
            index += 1
            print(f"\n{index:<5} {expense['name']:<15} {expense['amount']}")
            total += expense['amount']
    print(f"\nTotal: {total}\n")


def view_expenses():

    clear_terminal()

    if not expenses:
        print("No expenses found. Add an expense first.")
        return

    while True:
        section_heading('VIEW SELECTED')
        show_expense_view()
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Invalid Input, Enter only integers")

        if choice == 1:
            view_all_expenses()

        elif choice == 2:
            view_by_category()

        elif choice == 3:
            clear_terminal()
            break
        else:
            print("Choose correct option!")


def delete_expenses():
    if not expenses:
        clear_terminal()
        print("No expenses found.")
        return

    while True:
        if not expenses:
            break
        view_all_expenses()
        print(" 0 => Back")
        print("-1 => Delete ALL")
        while True:
            try:
                choice_to_delete = int(input("Choose expense No. to DELETE: "))
                break
            except ValueError:
                print("Invalid Input, Enter only integers")

        if choice_to_delete >= 1 and choice_to_delete <= len(expenses):
            toDelete = expenses[choice_to_delete-1]
            print(f"\n{toDelete['name']} - {toDelete['amount']} - {toDelete['category']}")

            while True:
                delete_confirmation = input("Delete this expense? (y/n): ")
                if delete_confirmation.lower() == 'y':
                    del expenses[choice_to_delete-1]
                    save_expenses()
                    clear_terminal()
                    print("Expense deleted successfully.")
                    break
                elif delete_confirmation.lower() == 'n':
                    print("Exiting DELETE")
                    break
                else:
                    print("Please enter 'y' or 'n'.")

        elif choice_to_delete == -1:
            while True:
                delete_confirmation = input("Delete this expense? (y/n): ")
                if delete_confirmation.lower() == 'y':
                    expenses.clear()
                    save_expenses()
                    clear_terminal()
                    print("Expense deleted successfully.")
                    break
                elif delete_confirmation.lower() == 'n':
                    print("Exiting DELETE")
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            break

        elif choice_to_delete == 0:
            clear_terminal()
            break
        else:
            print("Invalid option. Please choose an option from the list.")
            time.sleep(3)


def main():
    while True:
        show_menu()

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a whole number.")

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            print('Delete Selected')
            delete_expenses()

        elif choice == 4:
            clear_terminal()
            print('Goodbye! Thanks for using the Expense Tracker.')
            break

        else:
            print('Invalid Integer, Try again!')


if __name__ == "__main__":
    main()
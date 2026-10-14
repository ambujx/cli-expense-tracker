import json
import string
import os
import subprocess
from ui import section_heading 


def clear_terminal():
    # Identify the correct terminal command
    command = 'clear' if os.name == 'nt' else 'clear'
    
    # Execute securely using the subprocess module
    subprocess.run(command, shell=True)

def loadJSON():
    if not os.path.exists("expenses.json"):
        return []

    with open ("expenses.json", "r") as file:
        try:
            return json.load(file)
        except:
            return []

def dumpJSON():
    with open ("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


expenses = loadJSON()

categories = []

for item in expenses:
    category = item['category']
    if category not in categories:
        categories.append(category)


def showMenu():
    print()
    section_heading('CHOOSE OPERATION')
    print("1 -> Add Expense")
    print("2 -> View Expenses")
    print("3 -> Delete Expense")
    print("4 -> Exit")

def writeExpName():
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
            print("It can't be empty, Try again!")
            continue
        elif (typecheck == True):
            return expName
        elif(typecheck == False):
            print('Only string input allowed, Try again!')

def writeExpAmount():
    while True:
        while True:
            try:
                expAmount = float(input('\tAmount: '))
                break
            except ValueError:
                print('Amount should be a NUMBER, Try again!')
        if expAmount == 0:
            return 0
        elif expAmount > 0 and expAmount < 9999999999:
            return expAmount
        elif expAmount == 'inf':
            print("Amount can not be infinite!")
        else:
            print('Amount should be Greater than Zero, and not be infinite, Try again!')

def chooseCategory():

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
                    categoryOption = int(input("Choose your option: "))
                    break
                except ValueError:
                    print("Only integers are allowed, Try again!")

            if categoryOption == 0:
                expCategory = 0
                return expCategory
            
            if categoryOption >= 1 and categoryOption <= len(categories)+1:
                break
            else:
                print("Choose valid option as defined Above, Try again!")

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
                print('Only string input allowed, Try again!')
                continue
            elif(expCategory == ""):
                print("It can't be empty, Try again!")
                continue
            elif expCategory in categories:
                print(f"Category already present at: {categories.index(expCategory)+1}")
            else:   
                categories.append(expCategory)
                break
 
    elif categoryOption >= 1 and categoryOption <= len(categories):
        expCategory = categories[categoryOption-1]
    return expCategory

def addExpense():
    while True:
        clear_terminal()
        section_heading("ADD EXPENSE")

        print("0 -> Back")
        expName = writeExpName()
        if expName == 0:
            break

        expAmount = writeExpAmount()
        if expAmount == 0:
            break

        expCategory = chooseCategory()
        if expCategory == 0:
            break

        expense_dict = {
            'name': expName,
            'amount': expAmount,
            'category': expCategory
        }

        expenses.append(expense_dict)

        dumpJSON()

        clear_terminal()
        print('Expense added successfully!')
        break

def showExpenseView():
    print("1 -> View All")
    print("2 -> View By Category")
    print("3 -> Back")

def viewAllExpense():
    clear_terminal()
    totalAmount = 0
    section_heading("ALL EXPENSES")
    print(f"\n{'No.':<5}{'Expense':<15}{'Amount':<12}{'Category'}")

    for index, expense in enumerate(expenses, start=1):
        print(f"\n{index:<5} {expense['name']:<15} {expense['amount']:<12} {expense['category']}")
        totalAmount += expense['amount']
    print(f"\nTotal: {totalAmount}\n")

def viewByCategory():
    clear_terminal()
    section_heading("CHOOSE CATEGORY TO VIEW")
    for index,category in enumerate(categories, start=1):
        print(f"{index} -> {category}", end=" ")
        totalAmount = 0
        for expense in expenses:
            if expense['category'] == category:
                totalAmount += expense['amount']
        print(totalAmount)

    while True:
        while True:
            try:
                chooseCat = int(input("Choose your input: "))                
                break
            except ValueError:
                print("Invalid Input, Enter only integers")
        if chooseCat >=1 and chooseCat <= len(categories):
            break
        else:
            print("Choose valid option, Try again!")

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
    print (f"\nTotal: {total}\n")

def viewExpense():

    clear_terminal()

    if not expenses:
        print("No expense present, Create expense")
        return

    while True:
        section_heading('VIEW SELECTED')
        showExpenseView()
        while True:
            try:
                choice = int(input("Choose your input: "))                
                break
            except ValueError:
                print("Invalid Input, Enter only integers")

        if choice == 1:
            viewAllExpense()

        elif choice == 2:
            viewByCategory()

        elif choice == 3:
            clear_terminal()
            break
        else:
            print("Choose correct option!")


def delExpense():
    if not expenses :
        clear_terminal()
        print("No Expense Found")
        return

    while True:
        if not expenses:
            break
        viewAllExpense()
        print (" 0 => Back")
        print ("-1 => Delete ALL")
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
                delete_confirmation = input("Delete this expense? [y/n]:")
                if delete_confirmation.lower() == 'y':    
                    del expenses[choice_to_delete-1]
                    dumpJSON()
                    clear_terminal()
                    print("Deleted successfully")
                    break
                elif delete_confirmation.lower() == 'n':
                    print("Exiting DELETE")
                    break
                else:
                    print("Choose [y/n]! Try again!")

        elif choice_to_delete == -1:
            while True:
                delete_confirmation = input("Delete this expense? [y/n]:")
                if delete_confirmation.lower() == 'y':    
                    expenses.clear()
                    dumpJSON()
                    clear_terminal()
                    print("Deleted successfully")
                    break
                elif delete_confirmation.lower() == 'n':
                    print("Exiting DELETE")
                    break
                else:
                    print("Choose [y/n]! Try again!")
            break

        elif choice_to_delete == 0:
            clear_terminal()
            break
        else:
            print("Choose valid option, Try again!")         


def main():
    while True:
        showMenu()

        while True:
            try:
                choice = int(input("Choose your input: "))                
                break
            except ValueError:
                print("Invalid Input, Enter only integers")

        if choice == 1:
            addExpense()

        elif choice == 2:
            viewExpense()

        elif choice == 3:
            print('Delete Selected')
            delExpense()

        elif choice == 4:
            clear_terminal()
            print('Goodbye!')
            break

        else:
            print('Invalid Integer, Try again!')

if __name__ == "__main__":
    main()
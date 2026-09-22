import string

expenses = []

categories = []

def showMenu():
    print()
    print('Choose Operation:')
    print("1 -> Add Expense")
    print("2 -> View Expenses")
    print("3 -> Exit")

def writeExpName():
    while True:
        expName = input('\tExpense name: ')
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
        if expAmount > 0:
            return expAmount
        else:
            print('Amount should be Greater than Zero, Try again!')  


def chooseCategory():
    print("Choose a Category: ")
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
        if categoryOption >= 1 and categoryOption <= len(categories)+1:
            break
        else:
            print("Choose valid option as defined Above, Try again!")

    if categoryOption == len(categories)+1:
        while True:
            expCategory = input('\tNew category name: ')
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
    print('Add Expense:')

    expName = writeExpName()

    expAmount = writeExpAmount()

    expCategory = chooseCategory()

    expense_dict = {
        'name': expName,
        'amount': expAmount,
        'category': expCategory
    }

    expenses.append(expense_dict)
    print('Expense added successfully!')

def showExpenseView():
    print("1 -> View All")
    print("2 -> View By Category")
    print("3 -> Back")

def viewExpense():
    if not expenses:
        print("No expense present, Create expense")
        return

    while True:
        showExpenseView()
        while True:
            try:
                choice = int(input("Choose your input: "))                
                break
            except ValueError:
                print("Invalid Input, Enter only integers")
        
        if choice == 1:
            totalAmount = 0
            for index,expense in enumerate(expenses, start=1):
                print(f"\nExpense {index}")
                print(f"Name: {expense['name']}")
                print(f"Amount: {expense['amount']}")
                print(f"Category: {expense['category']}")
                totalAmount += expense['amount']
            print(f"\nTotal: {totalAmount}\n")

        elif choice == 2:
            print("Choose Category: ")
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
            print(f"\nExpenses of {target_category}:")
            index = 0
            total = 0
            for expense in expenses:
                if expense['category'] == target_category:
                    index += 1
                    print(f"\nExpense {index}")
                    print(f"Name: {expense['name']}")
                    print(f"Amount: {expense['amount']}")
                    print(f"Category: {expense['category']}")
                    total += expense['amount']
            print (f"\nTotal: {total}")

        elif choice == 3:
            break

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
            print('View Selected')
            viewExpense()

        elif choice == 3:
            print('Goodbye!')
            break

        else:
            print('Invalid Integer')

if __name__ == "__main__":
    main()
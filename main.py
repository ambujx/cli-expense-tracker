expenses = []

def showMenu():
    print('\n')
    print("1 -> Add Expense")
    print("2 -> View Expenses")
    print("3 -> Exit")

def inputDirection():
    while True:
        showMenu()

        while True:
            try:
                choice = int(input("Choose your input: "))                
                break
            except ValueError:
                print("Invalid Input, Enter only integers")


        if choice == 1:
            print('Add Expense:')

            while True:
                expName = input('\tExpense name: ')
                try:
                    expName = int(expName)
                except:
                    pass
                if isinstance(expName, int):
                    print('Only string input allowed, Try again!')
                elif(expName == ""):
                    print("It can't be empty, Try again!")
                else:
                    break

            while True:
                expAmount = input('\tAmount: ')
                try:
                    expAmount = int(expAmount)
                except:
                    pass
                if isinstance(expAmount, int) and expAmount > 0:
                    break
                else:
                    print('Amount should be INTEGER greater than Zero, Try again!')
                
            while True:
                expCategory = input('\tCategory: ')
                try:
                    expCategory = int(expCategory)
                except:
                    pass
                if isinstance(expCategory, int):
                    print('Only string input allowed, Try again!')
                elif(expCategory == ""):
                    print("It can't be empty, Try again!")
                else:
                    break


            expense_dict = {
                'name': expName,
                'amount': expAmount,
                'category': expCategory
            }

            expenses.append(expense_dict)
            print('Expense added successfully!')        

        elif choice == 2:
            print('View Selected')
            print(expenses)

        elif choice == 3:
            print('Goodbye!')
            break
            
        else:
            print('Invalid Integer')

if __name__ == "__main__":
    inputDirection()
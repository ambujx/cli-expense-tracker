expenses = []

def showMenu():
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
            print('Add Selected')

        elif choice == 2:
            print('View Selected')

        elif choice == 3:
            print('Goodbye!')
            break
            
        else:
            print('Invalid Integer')

if __name__ == "__main__":
    inputDirection()

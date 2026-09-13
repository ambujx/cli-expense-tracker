expenses = []

def showMenu():
    print("1 -> Add Expense")
    print("2 -> View Expenses")
    print("3 -> Exit")

def inputDirection():
    while True:
        showMenu()
        choice = int(input("Choose your input: "))

        if choice == 1:
            print('Add Selected')

        elif choice == 2:
            print('View Selected')

        elif choice == 3:
            print('Goodbye!')
            break
            
        else:
            print('Invalid input')

if __name__ == "__main__":
    inputDirection()

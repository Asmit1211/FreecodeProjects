# Function to add a new expense to the expenses list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Function to print all expenses with amount and category
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
        
# Function to calculate the total of all expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses based on a specific category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Main function to run the expense tracker program
def main():
    # List to store all expenses
    expenses = []
    
    # Infinite loop to keep the program running until user chooses to exit
    while True:
        # Display the menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Get the user's choice from the menu
        choice = input('Enter your choice: ')

        # Add a new expense
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        # List all expenses
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        # Show the total expenses
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        # Filter expenses by a specific category and list them
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        # Exit the program
        elif choice == '5':
            print('Exiting the program.')
            break

# Call the main function to start the program
main()

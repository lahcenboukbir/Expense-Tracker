# Adds a new expense to the expenses list.
def add_expense(expenses):
    # Prompt the user to enter the description of the expense
    description = input("Enter expense description: ")
    # Prompt the user to enter the amount of the expense and convert it to a float
    amount = float(input("Enter expense amount: "))
    # Append a dictionary with the description and amount to the expenses list
    expenses.append({"description": description, "amount": amount})

# Displays all the expenses in the expenses list.
def view_expenses(expenses):
    print("\nExpenses:")
    # Loop through each expense in the list and print the description and amount
    for expense in expenses:
        print(f"{expense['description']}: {expense['amount']:.2f} MAD")

# Displays the total amount of all expenses.
def view_summary(expenses):
    # Initialize total to 0
    total = 0
    # Loop through each expense in the list and add the amount to the total
    for expense in expenses:
        total += expense['amount']
    # Print the total amount spent
    print(f"\nTotal amount spent: {total:.2f} MAD")

# Main function to run the expense tracker program.
def main():
    # Initialize an empty list to store expenses
    expenses = []
    while True:
        # Display menu options
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        # Prompt the user to choose an option
        choice = input("Choose an option: ")

        # Handle the user's choice
        if choice == '1':
            # Call add_expense function to add a new expense
            add_expense(expenses)
        elif choice == '2':
            # Call view_expenses function to display all expenses
            view_expenses(expenses)
        elif choice == '3':
            # Call view_summary function to display the total amount spent
            view_summary(expenses)
        elif choice == '4':
            # Exit the loop and terminate the program
            break
        else:
            # Print an error message for invalid choice
            print("Invalid choice. Please try again.")

# Call the main function to run the program
main()

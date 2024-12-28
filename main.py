from account_login import create_or_login
from transactions import perform_transaction, view_mini_statement
from alerts import set_threshold
from reports import generate_bank_statement

def main_menu():
    while True:
        print("\nWelcome to Tushar's Mini Bank!")
        print("1. Create an Account / Login")
        print("2. Perform Transactions")
        print("3. View Mini-Statement")
        print("4. Set Alerts")
        print("5.Generate Bank Statement")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_or_login()
        elif choice == '2':
            perform_transaction()
        elif choice == '3':
            view_mini_statement()
        elif choice == '4':
            set_threshold()
        elif choice == '5':
            generate_bank_statement()
        elif choice == '6':
            print("Thank you for using Tushar's Mini Bank!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()

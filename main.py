from account_login import create_or_login
from transactions import perform_transaction, view_mini_statement
from alerts import set_threshold
from reports import generate_bank_statement
from colorama import init, Fore, Style

# Initialize Colorama
init()

def main_menu():
    """
    Displays the main menu for Tushar's Mini Bank and handles user selections 
    to perform various operations like account creation, transactions, 
    viewing statements, setting alerts, and generating bank statements.
    """
    while True:
        print(Fore.CYAN + "\nWelcome to Tushar's Mini Bank!")
        print(Fore.YELLOW + "1. Create an Account / Login")
        print(Fore.YELLOW + "2. Perform Transactions")
        print(Fore.YELLOW + "3. View Mini-Statement")
        print(Fore.YELLOW + "4. Set Alerts")
        print(Fore.YELLOW + "5. Generate Bank Statement")
        print(Fore.RED + "6. Exit" + Style.RESET_ALL)
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
            print(Fore.GREEN + "Thank you for using Tushar's Mini Bank!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()


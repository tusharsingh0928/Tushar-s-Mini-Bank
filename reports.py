import json
from datetime import datetime, timedelta
from account_login import login, load_accounts
import getpass

def generate_bank_statement():
    """
    Generates and displays a bank statement for the given account number.
    The statement includes transactions within a specified number of months.
    """
    account_number = input("Enter your account number: ")
    password = getpass.getpass("Enter your password: ")

    # Verify login
    if not login(account_number, password):
        print("Authentication failed.")
        return

    # Load accounts
    accounts = load_accounts()
    for account in accounts:
        if account["account_number"] == account_number:
            transactions = account.get("transactions", [])
            break
    else:
        print("Account not found.")
        return

    # Ask user for the number of months
    months = int(input("Enter the number of months for the bank statement: "))
    current_date = datetime.now()
    start_date = current_date - timedelta(days=months * 30)

    # Filter transactions based on the number of months
    filtered_transactions = [
        transaction for transaction in transactions 
        if datetime.fromisoformat(transaction["timestamp"]) >= start_date
    ]

    # Display the bank statement
    if filtered_transactions:
        print("\nBank Statement:")
        balance = account["balance"]
        final_balance = balance
        for transaction in filtered_transactions[::-1]:  # Display transactions in chronological order
            balance_change = transaction["amount"]
            final_balance -= balance_change
            print(f"Date: {transaction['timestamp']}, Description: {transaction['description']}, Amount: {transaction['amount']}, Balance after transaction: {final_balance:.2f}")

        print(f"\nFinal Balance: {account['balance']:.2f}")
    else:
        print("No transactions found within the specified period.")

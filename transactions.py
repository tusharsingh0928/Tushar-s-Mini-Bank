import json
from datetime import datetime
from account_login import login, load_accounts, save_to_json

def perform_transaction():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    # Verify login
    if not login(account_number, password):
        print("Authentication failed.")
        return

    # Load accounts
    accounts = load_accounts()
    for account in accounts:
        if account["account_number"] == account_number:
            break
    else:
        print("Account not found.")
        return

    print("\n1. Deposit")
    print("2. Withdrawal")
    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account["balance"] += amount
        description = "Deposit"
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if account["balance"] >= amount:
            account["balance"] -= amount
            description = "Withdrawal"
        else:
            print("Insufficient funds.")
            return
    else:
        print("Invalid choice.")
        return

    # Save transaction within the account
    transaction = {
        "timestamp": datetime.now().isoformat(),
        "description": description,
        "amount": amount
    }
    if "transactions" not in account:
        account["transactions"] = []
    account["transactions"].append(transaction)
    save_to_json(account)

    # Display remaining balance
    print(f"Remaining Balance: Rs{account['balance']:.2f}")

def view_mini_statement():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

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

    # Sort transactions by timestamp and display the last 5
    transactions.sort(key=lambda x: x['timestamp'], reverse=True)
    if transactions:
        print("\nLast 5 Transactions:")
        for transaction in transactions[:5]:
            print(f"{transaction['timestamp']}: {transaction['description']} - {transaction['amount']}")
    else:
        print("No transactions found.")

def set_threshold():
    print("Setting alerts is not yet implemented.")

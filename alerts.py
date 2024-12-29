import json
from account_login import load_accounts, save_to_json, login
import getpass

def set_threshold():
    """
    Prompts the user to set a custom threshold amount for their account.
    If the balance falls below this threshold, an alert is displayed.
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
            break
    else:
        print("Account not found.")
        return

    # Set custom threshold
    threshold = float(input("Enter your custom threshold amount: "))
    account["threshold"] = threshold
    save_to_json(account)
    print(f"Custom threshold set to ₹{threshold:.2f}")

    # Check balance and alert
    check_balance_alert(account)

def check_balance_alert(account):
    """
    Checks the account balance and displays an alert if it falls below 
    predefined limits (₹100) or the user's custom threshold.
    """
    balance = account["balance"]
    custom_threshold = account.get("threshold", float('inf'))

    if balance < 100:
        print("Alert: Your balance is below ₹100.")
    elif balance < custom_threshold:
        print(f"Alert: Your balance is below your custom threshold of ₹{custom_threshold:.2f}.")

import json
from account_login import load_accounts, save_to_json, login

def set_threshold():
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

    # Set custom threshold
    threshold = float(input("Enter your custom threshold amount: "))
    account["threshold"] = threshold
    save_to_json(account)
    print(f"Custom threshold set to ₹{threshold:.2f}")

    # Check balance and alert
    check_balance_alert(account)

def check_balance_alert(account):
    balance = account["balance"]
    custom_threshold = account.get("threshold", float('inf'))

    if balance < 100:
        print("Alert: Your balance is below ₹100.")
    elif balance < custom_threshold:
        print(f"Alert: Your balance is below your custom threshold of ₹{custom_threshold:.2f}.")

# def check_all_balances():
#     accounts = load_accounts()
#     for account in accounts:
#         check_balance_alert(account)

# def set_default_alerts():
#     accounts = load_accounts()
#     for account in accounts:
#         account["threshold"] = 100  # Set default threshold
#         save_to_json(account)
#         print(f"Default threshold of ₹100 set for account {account['account_number']}.")


import json
import random
import os
import datetime

def save_to_json(account_data, filename='accounts.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Check if the account already exists and update it
    for i, acc in enumerate(data):
        if acc['account_number'] == account_data['account_number']:
            data[i] = account_data
            break
    else:
        data.append(account_data)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_accounts(filename='accounts.json'):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_transaction(account_number, transaction):
    accounts = load_accounts()
    for account in accounts:
        if account["account_number"] == account_number:
            if "transactions" not in account:
                account["transactions"] = []
            account["transactions"].append(transaction)
            save_to_json(account)
            break

def create_or_login():
    print("\n1. Create an Account")
    print("2. Login with Existing Credentials")
    choice = input("Choose an option: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        user_login()
    else:
        print("Invalid choice. Try again.")

class CreateAccount:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.phone_number = ""
        self.address = ""
        self.balance = 0.0
        self.account_number = ""
        self.password = ""
        self.created_at = ""

    def get_user_details(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.email = input("Enter your email address: ")
        self.phone_number = input("Enter your phone number: ")
        self.address = input("Enter your address: ")
        self.balance = float(input("Enter your initial balance: "))
        self.created_at = datetime.datetime.now().isoformat()

    def generate_account_number(self):
        self.account_number = str(random.randint(10000000000, 99999999999))

    def get_user_password(self):
        self.password = input("Create a password: ")

    def mask_password(self):
        masked_password = '*' * (len(self.password) - 4) + self.password[-4:]
        return masked_password

    def display_user_details(self):
        print("\nAccount Details:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Account Number: {self.account_number}")
        print(f"Password: {self.mask_password()}")
        print(f"Account Created At: {self.created_at}")

def create_account():
    account = CreateAccount()
    account.get_user_details()
    account.generate_account_number()
    account.get_user_password()
    account.display_user_details()
    print("Account created successfully!")

    # Save account details to JSON
    account_data = {
        "first_name": account.first_name,
        "last_name": account.last_name,
        "email": account.email,
        "phone_number": account.phone_number,
        "address": account.address,
        "balance": account.balance,
        "account_number": account.account_number,
        "password": account.password,
        "created_at": account.created_at,
        "transactions": []  # Initialize with an empty list
    }
    save_to_json(account_data)

def login(account_number, password):
    accounts = load_accounts()
    for account in accounts:
        if account["account_number"] == account_number and account["password"] == password:
            print("Login successful!")
            return True
    print("Invalid account number or password.")
    return False

def user_login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    if login(account_number, password):
        print("Login successful!")
    else:
        print("Login failed.")

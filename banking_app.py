import streamlit as st
import json
from datetime import datetime, timedelta
from account_login import create_account, user_login, load_accounts, save_to_json
from transactions import perform_transaction, view_mini_statement
from alerts import set_threshold, check_balance_alert
from reports import generate_bank_statement

def main():
    st.title("Tushar's Mini Bank")

    menu = ["Home", "Create Account / Login", "Perform Transactions", "View Mini-Statement", "Set Alerts", "Generate Bank Statement"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to Tushar's Mini Bank!")
    elif choice == "Create Account / Login":
        create_or_login()
    elif choice == "Perform Transactions":
        perform_transactions()
    elif choice == "View Mini-Statement":
        view_mini_statement()
    elif choice == "Set Alerts":
        set_alerts()
    elif choice == "Generate Bank Statement":
        generate_bank_statement()

def create_or_login():
    st.subheader("Create Account / Login")

    option = st.selectbox("Select Option", ["Create Account", "Login"])

    if option == "Create Account":
        if st.button("Create Account"):
            create_account()
            st.success("Account created successfully!")

    elif option == "Login":
        account_number = st.text_input("Account Number")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            if user_login(account_number, password):
                st.success("Login successful!")
            else:
                st.error("Invalid account number or password.")

def perform_transactions():
    st.subheader("Perform Transactions")

    account_number = st.text_input("Account Number")
    password = st.text_input("Password", type='password')

    if st.button("Authenticate"):
        if user_login(account_number, password):
            st.success("Authenticated!")

            transaction_type = st.selectbox("Transaction Type", ["Deposit", "Withdrawal"])
            amount = st.number_input("Amount", min_value=0.0, format='%f')

            if st.button("Submit"):
                if transaction_type == "Deposit":
                    perform_transaction(account_number, password, "Deposit", amount)
                elif transaction_type == "Withdrawal":
                    perform_transaction(account_number, password, "Withdrawal", amount)

                st.success(f"{transaction_type} of ₹{amount:.2f} completed successfully!")

def view_mini_statement():
    st.subheader("View Mini-Statement")

    account_number = st.text_input("Account Number")
    password = st.text_input("Password", type='password')

    if st.button("View Mini-Statement"):
        if user_login(account_number, password):
            transactions = load_accounts()["transactions"]
            mini_statement = transactions[-5:]
            st.write("Last 5 Transactions:")
            for transaction in mini_statement:
                st.write(f"{transaction['timestamp']}: {transaction['description']} - ₹{transaction['amount']:.2f}")

def set_alerts():
    st.subheader("Set Alerts")

    account_number = st.text_input("Account Number")
    password = st.text_input("Password", type='password')

    if st.button("Authenticate"):
        if user_login(account_number, password):
            st.success("Authenticated!")

            threshold = st.number_input("Set Threshold Amount", min_value=0.0, format='%f')

            if st.button("Set Threshold"):
                set_threshold(account_number, threshold)
                st.success(f"Threshold set to ₹{threshold:.2f}")

def generate_bank_statement():
    st.subheader("Generate Bank Statement")

    account_number = st.text_input("Account Number")
    password = st.text_input("Password", type='password')
    months = st.number_input("Enter number of months", min_value=1, format='%d')

    if st.button("Generate Statement"):
        if user_login(account_number, password):
            generate_bank_statement(account_number, months)

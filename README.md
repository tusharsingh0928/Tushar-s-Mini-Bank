# Tushar-s-Mini-Bank

Welcome to Tushar's Mini Bank, a simplified banking system built using Python and Streamlit. This project allows users to create accounts, perform transactions, view mini-statements, set balance alerts, and generate bank statements.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Account Management**: Create an account and log in with credentials.
- **Transactions**: Perform deposits and withdrawals.
- **Mini-Statements**: View the last 5 transactions.
- **Alerts**: Set custom balance thresholds and receive alerts.
- **Bank Statements**: Generate bank statements for a specified period.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tusharsingh0928/tushars-mini-bank.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tushars-mini-bank
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run banking_app.py
    ```
2. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

## Project Structure

├── main.py 
├── account_login.py # Account creation and login management 
├── transaction.py# Handle deposits, withdrawals, and mini-statements 
├── alerts.py# Set balance thresholds and alerts 
├── reports.py# Generate bank statements 
├── banking_app.py # Streamlit GUI for the project 
├── requirements.txt# List of dependencies 
└── README.md# Project documentation


## Dependencies

- Streamlit==1.41.1

You can install these dependencies using the `requirements.txt` file provided in the project.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

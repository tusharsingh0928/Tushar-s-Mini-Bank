# Tushar's Mini Bank

Welcome to Tushar's Mini Bank, a simplified console-based banking system built using Python. This project allows users to create accounts, perform transactions, view mini-statements, set balance alerts, and generate bank statements through the command line interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Account Management**: Create an account and log in with credentials using secure password hashing with bcrypt.
- **Transactions**: Perform deposits and withdrawals.
- **Mini-Statements**: View the last 5 transactions.
- **Alerts**: Set custom balance thresholds and receive alerts.
- **Bank Statements**: Generate bank statements for a specified period.
- **Enhanced CLI**: Improved user experience with colored terminal text using colorama.

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

1. Run the main application script:
    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to create accounts, log in, perform transactions, view mini-statements, set alerts, and generate bank statements.

## Project Structure

├── account_login.py     # Account creation and login management 
├── transaction.py       # Handle deposits, withdrawals, and mini-statements 
├── alerts.py            # Set balance thresholds and alerts 
├── reports.py           # Generate bank statements 
├── main.py              # Main script to run the console-based application 
├── requirements.txt     # List of dependencies 
└── README.md            # Project documentation


## Dependencies

- Python 3.x
- bcrypt: For secure password hashing.
- getpass: For secure password input.
- colorama: For colored terminal text.

You can install any additional dependencies using the `requirements.txt` file provided in the project.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

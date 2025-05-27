  Banking App
A simple command-line banking application built with Python. This app allows users to:

Create a new bank account

Deposit funds into an account

Withdraw funds from an account

📁 Project Structure
csharp
Copy
Edit
banking_app/
├── __init__.py
├── main.py
├── account.py
└── ... (other supporting modules)
Pipfile
Pipfile.lock
🚀 Features
Create Account: Set up a new bank account with a name and starting balance.

Deposit Funds: Add money to your account balance.

Withdraw Funds: Take money out, with validation to prevent overdrafts.

🛠 Requirements
Python 3.8 or later

pipenv for managing dependencies


bash
Copy
Edit
pipenv install
Run the App
Use the following command to start the app:

pipenv run python3 -m banking_app.main
This will launch the CLI where you can create accounts, deposit, and withdraw funds.

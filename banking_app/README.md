# Banking App

## Overview
The Banking App is a command-line interface (CLI) application that allows users to manage their accounts, including creating accounts, depositing funds, and withdrawing funds. The application uses SQLAlchemy ORM for database management and Pipenv for dependency management.

## Features
- User account creation
- Deposit funds to user accounts
- Withdraw funds from user accounts
- Balance management

## Project Structure
```
banking_app
├── app
│   ├── __init__.py          # Initializes the application package
│   ├── cli.py               # CLI logic for user account management
│   ├── models.py            # SQLAlchemy ORM models
│   ├── database.py          # Database connection and session management
│   └── utils.py             # Utility functions for the application
├── tests
│   └── test_app.py          # Unit tests for the application
├── Pipfile                   # Project dependencies
├── Pipfile.lock              # Locked dependencies for consistent installations
├── README.md                 # Documentation for the project
└── main.py                   # Entry point for the application
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd banking_app
   ```

2. Install dependencies using Pipenv:
   ```
   pipenv install
   ```

3. Activate the virtual environment:
   ```
   pipenv shell
   ```

4. Run the application:
   ```
   python main.py
   ```

## Usage
- To create a new user account, use the command:
  ```
  python main.py create_account <username>
  ```

- To deposit funds, use the command:
  ```
  python main.py deposit <username> <amount>
  ```

- To withdraw funds, use the command:
  ```
  python main.py withdraw <username> <amount>
  ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
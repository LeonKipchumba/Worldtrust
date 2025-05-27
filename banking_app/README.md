# Banking App CLI

## Overview
This is a command-line banking application written in Python. It allows users to create accounts, deposit funds, and withdraw funds, all managed through a simple interactive menu. The app uses SQLAlchemy ORM for database management and follows best practices for Python CLI projects.

## Features
- User account creation
- Deposit funds to user accounts
- Withdraw funds from user accounts
- Persistent storage using SQLite and SQLAlchemy ORM
- Interactive menu navigation (no need to remember commands)
- Well-structured Python package
- Virtual environment managed with Pipenv

## Project Structure
```
banking_app/
├── app/
│   ├── __init__.py        # Main entry and menu loop
│   ├── cli.py             # CLI logic and menu
│   ├── database.py        # Database connection/session
│   ├── models.py          # SQLAlchemy ORM models
│   └── utils.py           # Utility functions
├── tests/
│   └── test_app.py        # Unit tests
├── main.py                # Entry point for the app
├── Pipfile                # Pipenv dependencies
├── Pipfile.lock           # Locked dependencies
├── README.md              # Project documentation
└── LICENSE                # License file
```

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd banking_app
   ```
2. **Install dependencies using Pipenv:**
   ```bash
   pipenv install
   ```
3. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```
4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage
- Follow the on-screen menu to create accounts, deposit, or withdraw funds.
- All data is stored in a local SQLite database (`banking_app.db`).

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
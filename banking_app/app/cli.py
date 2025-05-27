from banking_app.app.database import get_db  # fixed import
from banking_app.app.models import User  # fixed import

def create_account(username, initial_balance):
    """Create a new user account with an initial balance."""
    session = next(get_db())
    new_user = User(username=username, balance=initial_balance, password="password")
    session.add(new_user)
    session.commit()
    print(f"Account created for {username} with balance {initial_balance}.")

def deposit(username, amount):
    """Deposit funds into a user's account."""
    session = next(get_db())
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.balance += amount
        session.commit()
        print(f"Deposited {amount} to {username}'s account. New balance: {user.balance}.")
    else:
        print(f"User {username} not found.")

def withdraw(username, amount):
    """Withdraw funds from a user's account."""
    session = next(get_db())
    user = session.query(User).filter_by(username=username).first()
    if user:
        if user.balance >= amount:
            user.balance -= amount
            session.commit()
            print(f"Withdrew {amount} from {username}'s account. New balance: {user.balance}.")
        else:
            print(f"Insufficient funds in {username}'s account.")
    else:
        print(f"User {username} not found.")

def menu():
    print("\n==== Banking App Menu ====")
    print("1. Create Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")
    choice = input("Select an option: ").strip()
    if choice == '1':
        username = input("Enter username: ").strip()
        initial_balance = float(input("Enter initial balance: "))
        create_account(username, initial_balance)
    elif choice == '2':
        username = input("Enter username: ").strip()
        amount = float(input("Enter deposit amount: "))
        deposit(username, amount)
    elif choice == '3':
        username = input("Enter username: ").strip()
        amount = float(input("Enter withdrawal amount: "))
        withdraw(username, amount)
    elif choice == '4':
        print("Exiting...")
        exit()
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    while True:
        menu()
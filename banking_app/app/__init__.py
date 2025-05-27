from .database import init_db

def main():
    from banking_app.app.cli import menu
    init_db()
    while True:
        menu()
        again = input("\nReturn to main menu? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
def validate_amount(amount):
    """Validate that the amount is a positive number."""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError as e:
        raise ValueError("Invalid amount. Please enter a valid number.") from e

def format_balance(balance):
    """Format the balance to two decimal places."""
    return f"${balance:.2f}"

def prompt_user_input(prompt):
    """Prompt the user for input and return the trimmed response."""
    return input(prompt).strip()
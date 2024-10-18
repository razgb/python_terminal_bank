def print_divider():
    print("=" * 50)

def print_sandwich_dividers(str):
    print_divider()
    print(str)
    print_divider()
    print("\n")

def clear_terminal(n = 50):
    print("\n" * n)

def main_prints():
    print("Choose the following options:")
    print_divider()
    print("1. Create a new account.")
    print("2. Sign in an existing account.")
    print_divider()
    print("3. Exit program.\n")

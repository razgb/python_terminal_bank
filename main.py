from account import Account
from account_storage import Account_storage
from helper_functions import *

"""
print("2. Deposit to account.")
print("3. Withdraw from account.")
print("4. See past transactions.")
print("5. Delete an account.")
"""

def create_account_flow():
    clear_terminal(5)

    while True:
        print_sandwich_dividers("Account Signup: (enter q to quit)")

        first_name = input("Enter first name: ")
        if first_name == "q":
            print("\n")
            break

        last_name = input("Enter last name: ")
        if last_name == "q":
            print("\n")
            break

        account = Account(first_name, last_name)
        success = Account_storage.add_account(account)

        if success:
            print_sandwich_dividers("\nAccount creation successful.\n")
            break

def main():
    print_sandwich_dividers("Welcome to bank:")

    # infinite loop that only exits by either option 6 or just pressing ctrl + c!
    while True:
        main_prints()
        response = input("Enter option number to further proceed:\nChoice: ")
        print("\n")

        if response == "1":
            create_account_flow()
        elif response == "2":
            pass
        elif response == "3":
            print_sandwich_dividers("Thank you for choosing Bank as your financial provider.")
            break # exits the infinite while loop
        else:
            print("\nError. Invalid response.")
            response = input("\nEnter choice number to choose option:\nChoice: ")


# Makes sure main() is only called when file run directly!
if __name__ == "__main__":
    main()

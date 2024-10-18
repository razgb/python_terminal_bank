"""
This is a class that fetches, reads, and writes data from
a simple JSON file called accounts.json that contains one list (array)

-> No instances will be created for this class (centralizes control)

What's JSON?

JavaScript Object Notation is a simple format for
structuring data. It is easy for humans to read and write,
and it is easy for machines to parse and generate.

e.g. Would look like this for an array of objects:

[
    {
        first_name: "John"
        last_name: "Doe"
    },
    {
        first_name: "Lane",
        last_name: "Wagner"
    }
]

If you see something you don't understand, read the python docs!!!
Or ask ChatGPT.
"""

import json
import os

import account
from helper_functions import print_divider

class Account_storage:
    @classmethod
    def get_stored_data(cls):

        if not os.path.exists("./accounts.json"):
            print_divider()
            print("File either does not exist or path written incorrectly.")
            SystemExit()

        try:
            with open("./accounts.json", "r") as json_file:
                # parse file back into a python list.
                accounts = json.load(json_file)

            # cheeky way to check if a list is empty or doesn't exist
            if not accounts:
                return []

            return accounts

        except json.JSONDecodeError:
            print("""\nApp Error: Error reading from your file.
            File may not be in valid json format. """)
            SystemExit()

        except Exception as e:
            print(f"An unexpected error while reading file \nError:\n{e}")
            SystemExit()

    @classmethod
    # account parameter is an account.py instance
    def add_account(cls, account):
        account_as_dict = account.get_details_dict()
        stored_accounts = cls.get_stored_data()

        if not isinstance(stored_accounts, list):
            print_divider()
            SystemExit("stored_accounts variable is not a list type.")
            return # if I don't add this - pyright will complain. why?

        stored_accounts.append(account_as_dict)

        try:
            # stringify list (array) back into json format
            with open("./accounts.json", "w") as json_file:
                #        (data, file_path, indentation)
                json.dump(stored_accounts, json_file, indent=4)
        except Exception:
            return False
        else:
            return True

    @classmethod
    def delete_account(cls, account):
        stored_accounts = cls.get_stored_data()
        account_number = account.get_account_number()

        if not isinstance(stored_accounts, list):
            print_divider()
            SystemExit("stored_accounts variable is not a list type.")
            return # if I don't add this - pyright will complain. why?

        account_deleted = False

        for i in range(len(stored_accounts)):
            acc = stored_accounts[i]

            if account_number == acc.get_account_number():
                del stored_accounts[i]
                account_deleted = True
                break

        if account_deleted == False:
            raise Exception("Seems this account doesn't exist or has been deleted.")

        return True

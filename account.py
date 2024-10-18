from transaction import Transaction
from random import randint

class Account:
    def __init__(self, first_name, last_name, balance = 0, ):
        self.__balance = balance
        self.__first_name = first_name
        self.__last_name = last_name

        # doubt anyone will create more than 1000 accounts in this program lmao
        self.__account_number = randint(0, 1_000)

        # will contain transaction class instances - not integers
        self.__past_transactions = [] # TODO: fetch past transactions from local json storage


    def __str__(self):
        return f"Account Holder: {self.__first_name} {self.__last_name} -- {self.__account_number}"


    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"


    def get_details_dict(self):
        transactions_as_dicts = []

        for t in self.__past_transactions:
            t_as_object = {
                "date": t.get_date(),
                "unix_date": t.get_unix_date(),
                "amount": t.get_amount(),
                "type": t.get_type()
            }

            transactions_as_dicts.append(t_as_object)

        return {
            "balance": self.__balance,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "account_number": self.__account_number,
            "past_transactions": transactions_as_dicts
        }


    def deposit(self, amount):
        if type(amount) != int:
            raise Exception("Error. Deposited value is not an integer.")
        elif amount <= 0:
            raise Exception("Cannot deposit zero or negative amount.")

        self.__balance += amount
        t = Transaction("deposit", amount)
        self.__past_transactions.append(t)

        return f"{amount} has been deposited successfully."

    def withdraw(self, amount):
        if type(amount) != int:
            raise Exception("Error. Deposited value is not an integer.")
        elif amount <= 0:
            raise Exception("Cannot withdraw zero or negative amount.")
        elif amount > self.__balance:
            raise Exception("Cannot withdraw more than account balance.")

        self.__balance -= amount
        t = Transaction("withdraw", amount)
        self.__past_transactions.append(t)

        return f"{amount} has been withdrawed successfully."

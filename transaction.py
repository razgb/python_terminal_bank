import datetime

class Transaction:
    def __init__(self, type, amount, date = None, unix_date = None):
        self.__type = type
        self.__amount = amount

        now = datetime.datetime.now()
        self.__date = now.strftime("%d/%m/%Y")
        self.__unix_date = now.timestamp()

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__type

    def get_date(self):
        return self.__unix_date

    def get_unix_date(self):
        return self.__unix_date

    # Shows a nice message with the transaction data, instead of "object at 0xfd832a"!
    def __str__(self):
        return f"{self.__type} -- {self.__amount} -- {self.__date}"

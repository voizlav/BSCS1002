class BankAccount:
    def __init__(self, owner: str, account: str, balance: float):
        self.__owner = owner
        self.__account = account
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    def __service_charge(self):
        self.__balance -= self.__balance / 100

    @property
    def balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

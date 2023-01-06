from abc import ABC, abstractmethod
from datetime import datetime


class AccountBase(ABC):
    """
    Abstract base class for account.
    """

    def __init__(self, account_name: str, bank_name: str, balance: float = 0 ) -> None:
        """
        Initialization method for AccountBase subclasses.
        """

        self._account_name = account_name
        self._bank_name = bank_name
        self._created = datetime.now()
        self._updated = None
        self._balance = balance

    def withdraw(self, amount: float) -> None:
        """
        method to make withdrawals.
        """

        if self._balance >= amount:
            self._balance -= amount
            self._created = datetime.now()
            print(f"Detail: ₦{amount} succesfully withdrawn.")
        else:
            print("Withdrawal failed")

    @abstractmethod
    def deposit(self, amount: float):
        """
        Abstract method to make deposit. To be implemented by subclasses.
        """

        pass

    def balance(self):
        """
        Method to return blance of account
        """

        return self._balance

    def info(self):
        print(f"Bank name: {self._bank_name}")
        print(f"Account name: {self._account_name}")
        print(f"Account balance: ₦{self._balance}")
        print(f"Account created at: {self._created}")
        print(f"Account updated at: {self._updated}")


class AdultAccount(AccountBase):
    """
    Adult account class
    """

    def deposit(self, amount: float):
        """
        AdultAccount implementation of deposit.
        """

        self._balance += amount
        self._created = datetime.now()
        print("Deposit succesful")


class StudentAccount(AccountBase):
    """
    Student account class
    """

    ACCOUNT_LIMIT = 4E5

    def deposit(self, amount: float):
        """
        StudentAccount implementation of deposit.
        """

        if (self._balance + amount) > self.ACCOUNT_LIMIT:
            print("Account limit exceeded.")
        else:
            self._balance += amount
            self._updated = datetime.now()
            print("Deposit succesful")


class Bank:
    """
    Factory class for Account class.
    A Bank can create Accounts.
    """

    def __init__(self, name: str):
        """
        Initialization method for bank.
        """

        self._name = name
        self._accounts: list[AccountBase] = []

    def create_adult_account(self, account_name: str, initial_deposit: float) -> AccountBase:
        """
        Factory method to create AdultAccount
        """

        acct = AdultAccount(account_name, self._name, initial_deposit)
        self._accounts.append(acct)
        return acct

    def create_student_account(self, account_name: str, initial_deposit: float) -> AccountBase:
        """
        Factory method to create StudentAccount
        """

        acct = StudentAccount(account_name, self._name, initial_deposit)
        self._accounts.append(acct)
        return acct

    def list_accounts(self) -> list[AccountBase]:
        """
        Return list of accounts in Bank.
        """

        return self._accounts

    def total_amount(self) -> float:
        """
        Return total amount in bank.
        """

        total = sum([acct.balance() for acct in self._accounts])
        return total


if __name__ == '__main__':
    b = Bank(name="ebank")
    acct1 = b.create_adult_account(account_name="Eteims", initial_deposit=40000)
    acct2 = b.create_student_account(account_name="Jacob", initial_deposit=4000)

    for acct in b.list_accounts():
        acct.info()

    print(f"Bank total balance: {b.total_amount()}")
    acct1.deposit(8000)
    print(f"Bank total balance: {b.total_amount()}")

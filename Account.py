from abc import ABC, abstractmethod


class Account:
    def __init__(self, holder_name, email, password, accountNo, account_type) -> None:
        self.account_name = holder_name
        self.email = email
        self.__password = password
        self.__accountNo = accountNo
        self.__balance = 0
        self.account_type = account_type

    @abstractmethod
    def account_info(self):
        print(f"Account holder: {self.account_name}, Balance {self.balance}")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance += amount

    def change_name(self, name):
        self.account_name = name
        print("Your account name change successfully!!!")

    def change_password(self, password):
        self.__password = password
        print("Your password change successfully!!!")


class SavingAccount(Account):
    def __init__(self, holder_name, email, password, accountNo, account_type, interest, year) -> None:
        self.year = year
        self.interest = interest
        super().__init__(holder_name, email, password, accountNo, account_type)

    def add_money(self, amount):
        if amount > 0:
            interestCal = (amount * self.interest) / 100
            self.balance += amount + interestCal
            print(f"Amount added successfully!!!.Your current  balance {self.balance}")
        else:
            print("Negative amount is not valid!!!")
            raise ValueError

    def withdraw_money(self, amount, year_of_account):
        if self.year < year_of_account:
            print(
                f"You are not able to witdraw before {self.year}. You need to wait {self.year - year_of_account}")

        else:
            if self.balance < amount:
                print(
                    f"Insufficient balance. Your current balance is {self.balance}")
            else:
                self.balance -= amount
                print(
                    f"Withdraw successfully!!! amount: {amount}. Current balance now {self.balance}")

    def account_info(self):
        print(
            f"Account holder: {self.account_name}, Balance {self.balance}, account_type {self.account_type}")


class SpecialAccount(Account):
    def __init__(self, holder_name, email, password, accountNo, account_type, withdray_limit) -> None:
        self.withdraw_limit = withdray_limit
        super().__init__(holder_name, email, password, accountNo, account_type)

    def account_info(self):
        print(
            f"Account holder: {self.account_name}, Balance {self.balance}, account_type {self.account_type}")

    def withdraw_money(self, amount):
        if amount > self.withdraw_limit:
            print(
                f"Your are not able to withdray more than {self.withdraw_limit}")
        else:
            self.balance -= amount
            print(f"Your current account balance is {self.balance}")

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(
                f"Your amount added successfull. Your current balance is {self.balance}")
        else:
            print("Negative amount is not valid")
            raise ValueError

from Account import Account, SavingAccount, SpecialAccount


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)
            return account
        else:
            print("Your account is not valid")
            raise ValueError


sonali_bank = Bank("Sonali")

while True:
    current_account = None
    if current_account is None:
        option = input("Please select Login(L) or Register(R)")
        if option == "R":
            holder_name = input("Enter your name: ")
            email = input("Enter your email: ")
            # password, accountNo, account_type
            password = input("Enter your password: ")
            accountNo = input("Enter your account no: ")
            account_type = input(
                "Enter the account type:- saving(SV)/special(SP): ")
            if account_type == "SV":
                interest = int(input("Enter the interest rate: "))
                year_of_interest = int(input("Entert the year of interest: "))
                account = SavingAccount(holder_name, email, password, accountNo,
                                        account_type="saving", interest=interest, year=year_of_interest)
                ac = sonali_bank.add_account(account)
                current_account = ac
                print("Your account created successfully")
            elif account_type == "SP":
                withdray_limit = int(input("Enter the limit of withdraw: "))
                account = SpecialAccount(
                    holder_name, email, password, accountNo, withdray_limit, account_type="special")
                ac = sonali_bank.add_account(account)
                current_account = ac
    else:
        print("bangla")

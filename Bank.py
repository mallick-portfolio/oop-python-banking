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

    def check_account(self, email, password):
        flag = False
        ac = None
        for account in self.__accounts:
            if account['email'] == email and account['password'] == password:
                flag = True
                ac = account
                break
        if flag:
            return ac
        else:
            print(
                f"Your {email} and {password} doesn't match with any account. Please provide valid information")
            raise ValueError


sonali_bank = Bank("Sonali")

while True:
    current_account = None
    if current_account is None:
        option = input("Please select Login(L) or Register(R)")
        if option == "R":
            holder_name = input("Enter your name: ")
            email = input("Enter your email: ")
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
                print("Your account created successfully")
        elif option == "L":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            ac = sonali_bank.check_account(email, password)
            current_account = ac

    else:
        if current_account.account_type == 'saving':
            print("========= ******* =========")
            print("1. Withdraw ")
            print("2. Deposit ")
            print("3. Show info ")
            print("4. Change info ")
            print("5. Change password ")
            print("6. Exit ")
            print("========= ******* =========")
            print()
            ch = int(input("Enter the option: "))
            if ch == 1:
                amount = int(input("Enter the amount: "))
                year_of_account = int(input("Running year of your account: "))
                current_account.withdraw_money(amount, year_of_account)
            elif ch == 2:
                amount = int(input("Enter the amount: "))
                current_account.add_money(amount)
            elif ch == 3:
                current_account.account_info()
            elif ch == 4:
                name = input("Enter your new account name: ")
                current_account.change_name(name)
            elif ch == 5:
                password = input("Enter your new password: ")
                current_account.change_password(password)
            elif ch == 6:
                current_account = None

        elif current_account.account_type == 'special':
            print("========= ******* =========")
            print("1. Withdraw ")
            print("2. Deposit ")
            print("3. Show info ")
            print("4. Change info ")
            print("5. Change password ")
            print("6. Exit ")
            print("========= ******* =========")
            print()
            ch = int(input("Enter the option: "))
            if ch == 1:
                amount = int(input("Enter the amount: "))
                current_account.withdraw_money(amount)
            elif ch == 2:
                amount = int(input("Enter the amount: "))
                current_account.add_money(amount)
            elif ch == 3:
                current_account.account_info()
            elif ch == 4:
                name = input("Enter your new account name: ")
                current_account.change_name(name)
            elif ch == 5:
                password = input("Enter your new password: ")
                current_account.change_password(password)
            elif ch == 6:
                current_account = None
        

import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number  = self.generate_account_number()
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be positive")
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account {account_number} created")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found")
        print(f"Account number: {account.account_number}")
        print(f"Name: {account.name}")
        print(f"Balance {account.balance}")
    
    def deposit(self, account_number, amount):
        if amount < 0:
            raise ValueError("Deposit must be a positive number")
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found")
        account.deposit(amount)
        self.save_to_file()
        print(f"Deposited {amount}, Balance: {account.balance}")

    def withdraw(self, account_number, amount):
        if amount < 0:
            raise ValueError("Withdraw must be a positive number")
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found")
        account.withdraw(amount)
        self.save_to_file()
        print(f"Withdrew {amount}, Balance: {account.balance}")

    def generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(5)
    
    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(
                {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, f
            )
            
    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.accounts = {
                    acc_num: Account.from_dict(acc_data)
                    for acc_num, acc_data in data.items()
            }
        except FileNotFoundError:
            self.accounts = {}

if __name__  == "__main__":
    bank = Bank()
    while True:
        print("\nBank application menu")
        print("1. Create account")
        print("2. View account")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit amount: "))
                bank.create_account(name, initial_deposit)
            except ValueError as e:
                print(f"Error: {e}")
           
        elif choice == "2":
            account_number = input("Enter account number: ")
            try: 
                bank.view_account(account_number)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            account_number = input("Enter account number: ")       
            try: 
                amount = float(input("Enter an deposit amount: "))
                bank.deposit(account_number, amount)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            account_number = input("Enter account number: ")       
            try: 
                amount = float(input("Enter an withdraw amount: "))
                bank.withdraw(account_number, amount)
            except ValueError as e:
                print(f"Error: {e}") 

        elif choice == "5":
            print("Exiting")
            break
            
        else:
            print("Invalid input. Enter from 1-5")

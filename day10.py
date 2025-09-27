# Simple Bank System 


class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ₱{amount}")
            return f"Deposited ₱{amount}. New balance: ₱{self.balance}"
        else:
            return "Invalid amount!"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ₱{amount}")
            return f"Withdrew ₱{amount}. New balance: ₱{self.balance}"
        else:
            return "Insufficient funds or invalid amount!"
    
    def check_balance(self):
        return f"Balance: ₱{self.balance}"
    
    def view_transactions(self):
        if not self.transactions:
            return "No transactions yet."
        
        transaction_history = "\nTransaction History:\n"
        for transaction in self.transactions:
            transaction_history += f"   {transaction}\n"
        return transaction_history

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001
    
    def create_account(self):
        print("\nCreate New Account")
        name = input("Enter account holder name: ")
        initial_deposit = float(input("Enter initial deposit: ₱"))
        
        account_num = self.next_account_number
        self.next_account_number += 1
        
        new_account = BankAccount(account_num, name, initial_deposit)
        self.accounts[account_num] = new_account
        
        print(f"Account created successfully!")
        print(f"   Account Number: {account_num}")
        print(f"   Account Holder: {name}")
        print(f"   Initial Balance: ₱{initial_deposit}")
    
    def find_account(self, account_number):
        return self.accounts.get(account_number)
    
    def deposit_money(self):
        acc_num = int(input("Enter account number: "))
        account = self.find_account(acc_num)
        
        if account:
            amount = float(input("Enter amount to deposit: ₱"))
            print(account.deposit(amount))
        else:
            print("Account not found!")
    
    def withdraw_money(self):
        acc_num = int(input("Enter account number: "))
        account = self.find_account(acc_num)
        
        if account:
            amount = float(input("Enter amount to withdraw: ₱"))
            print(account.withdraw(amount))
        else:
            print("Account not found!")
    
    def check_balance(self):
        acc_num = int(input("Enter account number: "))
        account = self.find_account(acc_num)
        
        if account:
            print(account.check_balance())
        else:
            print("Account not found!")
    
    def view_transactions(self):
        acc_num = int(input("Enter account number: "))
        account = self.find_account(acc_num)
        
        if account:
            print(account.view_transactions())
        else:
            print("Account not found!")

def main():
    bank = BankSystem()
    
    while True:
        print("\n" + "="*50)
        print("SIMPLE BANK SYSTEM")
        print("="*50)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")
        print("="*50)
        
        choice = input("Choose option (1-6): ")
        
        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            bank.view_transactions()
        elif choice == '6':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
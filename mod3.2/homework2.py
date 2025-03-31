'''
Homework2  
Name: Travis Routhier  
GitHub link: https://github.com/Tarsum67/Python/tree/main/mod3.2/homework2  
Note: Remember to use comments for each function.  
doc strings should include what each input consists of,  
what the expected output is and a description of the function.  
'''


class Bank_Account:
    def __init__(self, name, starting_amount):
        """
        Initialize a bank account with a name and starting amount.


        """
        self.name = name
        self.account = starting_amount

    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"

    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"

    def deposit(self, amount):
        """
        Deposit money into the account.

        """
        if amount > 0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print("Please deposit a positive number.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if amount > 0:
            if self.account - amount >= 0:
                self.account -= amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print("Insufficient funds.")
        else:
            print("Please withdraw an amount greater than zero.")

    def check_balance(self):

        print(f"Balance: {self.account}")


class SavingsAccount(Bank_Account):
    def __init__(self, name, balance, interest_rate=1.0):
        """
        Initialize a savings account.


        """
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def __repr__(self):
        return f"SavingsAccount(account_holder='{self.name}', balance={self.account}, interest_rate={self.interest_rate}%)"

    def __str__(self):
        return f"Savings Account - {self.name}: Balance = ${self.account:.2f}, Interest Rate = {self.interest_rate}%"

    def apply_interest(self):
        """
        Apply interest to the account balance based on the interest rate.
        """
        interest = self.account * (self.interest_rate / 100)
        self.account += interest
        return round(self.account, 2)


class CheckingAccount(Bank_Account):
    def __init__(self, name, balance, overdraft_limit=100.0):
        """
        Initialize a checking account.

        """
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def __repr__(self):
        return f"CheckingAccount(account_holder='{self.name}', balance={self.account}, overdraft_limit={self.overdraft_limit})"

    def __str__(self):
        return f"Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit = ${self.overdraft_limit:.2f}"

    def withdraw(self, amount):
        """
        Withdraw money from the account, considering the overdraft limit.

        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.account + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.account -= amount
            return round(self.account, 2)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))

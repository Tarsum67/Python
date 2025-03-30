'''
Homework1
Name:Travis Routhier
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self, name, starting_amount):
        self.name = name
        self.account = starting_amount

    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"

    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"

    def deposit(self, amount):
        if amount > 0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print("Please deposit a positive number.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please withdraw an amount greater than zero.")
        elif amount > self.account:
            print("Insufficient funds.")
        else:
            self.account -= amount
            print(f"{amount} withdrawn. New balance: {self.account}")

    def check_balance(self):
        print(f"Balance: {self.account}")


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))

'''
Homework1  
Name: Travis Routhier  
GitHub link: https://github.com/Tarsum67/Python/tree/main/mod3.2  
Note: Remember to use comments for each function.  
Docstrings should include what each input consists of,  
what the expected output is, and a description of the function.
'''


class Bank_Account:
    def __init__(self, name, starting_amount):
        """
        Initializes the bank account with a name and starting amount.

        """
        self.name = name
        self.account = starting_amount

    def __repr__(self):
        """
        Returns the formal string representation of the Bank_Account object.

        """
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"

    def __str__(self):
        """
        Returns a user-friendly string with the account name and balance.

        """
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"

    def deposit(self, amount):
        """
        Adds money to the account if the amount is positive.

        """
        if amount > 0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print("Please deposit a positive number.")

    def withdraw(self, amount):
        """
        Withdraws money from the account if funds are sufficient and amount is positive.

        """
        if amount <= 0:
            print("Please withdraw an amount greater than zero.")
        elif amount > self.account:
            print("Insufficient funds.")
        else:
            self.account -= amount
            print(f"{amount} withdrawn. New balance: {self.account}")

    def check_balance(self):
        """
        Prints the current account balance.

        """
        print(f"Balance: {self.account}")


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))

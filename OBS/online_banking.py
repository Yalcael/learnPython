class Account:
    def __init__(self, name: str, account_number: str, account_balance: float) -> None:
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance
        # The class keyword declares an Account class.
        # The __init__() method is the constructor, defined with the special double underscore notation at the beginning and end.
        # Self is a reference to the instance of the class. It is the first parameter of all instance methods in Python.
        # Name is the name of the account holder.
        # account_number is a unique identifier for the savings account, and balance are parameters passed to the constructor.
        # Inside the constructor self.name, self.account_number amd self.balance are attributes of the class Account that are initialized with the values of name,
        # account_number and balance.

    def deposit(self, amount: float) -> None:
        self.account_balance += amount
        print(f" Account {self.name} deposited {self.account_balance} $. Account balance {self.account_balance}")
        # The deposit method allows users to add funds to their account.
        # The method takes an additional parameter amount, which is the amount to be deposited.
        # Inside the method, the amount is added to the current balance using self.balance += amount.
        # A message is printed showing the depositor name and the amount deposited and the balance is updated.

    def withdraw(self, amount: float) -> None:
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{self.name} withdrawn {amount} $. Account balance is: {self.account_balance}")
        else:
            print("You don't have enough money to withdraw")
        # The withdrawals method allows users to withdraw funds from their account.
        # The method also takes an amount parameter which is the amount our user wants to withdraw.
        # The method checks if the account balance (self.balance) is greater than or equal to the amount our user wants to withdraw.
        # If the balance is enough, the withdrawal amount is removed from the balance using self.balance -= amount.
        # If the balance is not enough, a message stating "You don't have enough funds to withdraw" is printed to the user.


class SavingsAccount(Account):
    def __init__(self, name: str, account_number: str, account_balance: float, interest_rate: float) -> None:
        super().__init__(name, account_number, account_balance)
        self.interest_rate = interest_rate
    # The __init__ method is the constructor for the saving account class.
    # It accepts four parameters: name, which is the name of the account holder, account_number, which is a unique identifier for the savings account,
    # balance which is the initial balance of the account, and interest_rate which is the annual interest rate for the account.
    # The super().__init__(name, account_number, account_balance) line calls the constructor of the parent class (Account) to initialize the account number and balance.
    # The self.interest_rate = interest_rate line sets the interest rate specific to the savings account. It is not inherited.

    def add_interest(self) -> None:
        interest = self.account_balance * self.interest_rate
        self.deposit(interest)
    # The add_interest method calculates and adds interest to the account balance.
    # The method calculates the interest, by multiplying the current balance(self.account_balance_ with the interest rate (self.interest_rate).
    # The result is stored in the interest variable.
    # Finally, the self.deposit(interest) line calls the deposit method (defined in the parent Account class) to add the interest amount to the account balance.


def main() -> None:
    account_1: Account = Account("Vincent Lemaire", "24398AB", 3000)
    account_1.deposit(500)
    account_1.withdraw(200)

    savings_account: SavingsAccount = SavingsAccount("Vincent Lemaire", "24398AB", 300, 0.10)
    savings_account.deposit(1000)
    savings_account.add_interest()
    savings_account.withdraw(500)
    savings_account.withdraw(1000)


if __name__ == "__main__":
    main()

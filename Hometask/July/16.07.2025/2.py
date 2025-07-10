class BankAccount:
    def __init__(self):
        self.__balance =  0

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        return deposit_amount
    
    def withdraw(self, withdraw_amount):
        if self.__balance < withdraw_amount:
            print("Недостаточно средств") 
        else:
            self.__balance = self.__balance - withdraw_amount

    
account = BankAccount()
account.deposit(100)
print(account.balance)
account.withdraw(30)
print(account.balance)
account.withdraw(100)     


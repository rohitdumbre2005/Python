class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance


    def __str__(self):
        return f"{self.name}: ${self.balance}"

    
account=BankAccount("Alice",1000)
print(account)
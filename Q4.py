# -*- coding: utf-8 -*-
"""
Created on Fri May 24 22:11:55 2024

@author: FX-tec
"""


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest applied. Current balance: ${self.balance}")

    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance}, Interest rate: {self.interest_rate}%"


bank_account = BankAccount("55555", "Mohammad")
bank_account.deposit(1000)
bank_account.withdraw(500)
print(f"Final balance: ${bank_account.get_balance()}")

savings_account = SavingsAccount("66666", "Ahmad", interest_rate=1.5)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)

#!/usr/bin/env python3
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.card_payments_count = 0
        self.card_payments_total = 0
        self.monthly_card_payments = {}

    def process_transaction(self, amount, date):
        if amount < 0:  
            self.balance += amount
            self.card_payments_count += 1
            self.card_payments_total += amount
            month = date[:7]
            if month not in self.monthly_card_payments:
                self.monthly_card_payments[month] = 1
            else:
                self.monthly_card_payments[month] += 1

        else:  
            self.balance += amount

    def deduct_monthly_fee(self):
        if self.card_payments_count < 3 or self.card_payments_total < 100:
            self.balance -= 5 

    def calculate_final_balance(self):
        self.deduct_monthly_fee()
        return self.balance


def solution(A, D, N):
    bank_account = BankAccount()

    for i in range(N):
        amount = A[i]
        date = D[i]
        bank_account.process_transaction(amount, date)

    bank_account.deduct_monthly_fee()

    return bank_account.calculate_final_balance()


transactions_amounts = [-10, 20, -30, 50, -5]
transactions_dates = ['2020-01-01', '2020-02-15', '2020-02-20', '2020-03-01', '2020-12-31']
result = solution(transactions_amounts, transactions_dates, len(transactions_amounts))
print(f"Final Balance: {result}")

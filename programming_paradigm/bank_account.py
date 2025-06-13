# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # تعريف الرصيد الابتدائي للحساب البنكي
        self.account_balance = initial_balance
    
    def display_balance(self):
        # طباعة الرصيد الحالي بصيغة واضحة
        print(f"Current Balance: ${float(self.account_balance)}")


    def deposit(self, amount):
        # إيداع مبلغ في الحساب
        self.account_balance += amount

    def withdraw(self, amount):
        # سحب مبلغ من الحساب إذا كان الرصيد كافياً
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            # إذا لم يكن هناك رصيد كافٍ، لا يتم السحب
            return False

    
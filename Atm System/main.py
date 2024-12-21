class Atm:
    def __init__(self):
        self.user_pin = ''
        self.balance = 0
        self.create_pin()
    
    def create_pin(self):
        user_pin = int(input('Enter Your Pin'))
        self.user_pin = user_pin
    
    def check_balance(self):
        print(self.balance)
    
    def deposit_amount(self):
        amt = int(input('Enter the amount you want to deposit?'))
        self.balance += amt
        print(f'Amount Successfully deposited! \n Your current balance is {self.balance}')
    
    def withdraw_amount(self):
        amt = int(input('Enter the amount you want to withdraw:'))
        if amt > self.balance:
            print('Sorry insufficient balance!')
        else:
            self.balance -= amt
            print(f'Amount withdrawn successfully!\nBalance remaining: {self.balance}')
    
    def change_pin(self):
        old_pin = int(input('Enter your old pin'))
        if old_pin == self.user_pin:
            new_pin = int(input('Enter Your new pin'))
            self.user_pin = new_pin
        else:
            print('Sorry incorrect pin')

obj1 = Atm()
obj1.deposit_amount()
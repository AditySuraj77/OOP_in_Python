class Atm:

    def __init__(self):

        self.pin = ''
        self.balance = 0

        self.menu()

    def menu(self):

        user_input = input('''
                            Hello how would you like to proceed
                            1. Enter 1 Create Pin
                            2. Enter 2 to Deposit
                            3. Enter 3 to WithDraw
                            4. Enter 4 to Check Balance
                            5. Enter 5 to Exit
            ''')

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('Exit')

    def create_pin(self):
        print('Create Pin')
        self.pin = input('Enter Your pin : ')
        print('Pin Set Sucessfully')
        self.menu()

    def deposit(self):
        print('Deposit your Amount')
        temp = input('Enter Pin : ')
        if temp == self.pin:
            amount = int(input('Enter Amount : '))
            self.balance = self.balance + amount   # 2nd method self.balance += amount
        else:
            print('Invalid PIn')
        self.menu()

    def withdraw(self):
        print('Withdraw your amount')
        temp = input('Enter Pin : ')
        if temp == self.pin:
            amount = int(input('Enter Amount : '))
            if amount < self.balance:
                self.balance = self.balance - amount ## 2nd method self.balance -= amount
                print('WithDraw Sucessfully')
            else:
                print('Insufficient Amount')
        else:
            print('Invalid Pin')
        self.menu()

    def check_balance(self):
        print('Check Balance')
        temp = input('Enter Pin : ')
        if temp == self.pin:
            print(self.balance)
        else:
            print('Invalid Pin')
        self.menu()

sbi = Atm()



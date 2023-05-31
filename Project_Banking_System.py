class Bank:

    def __init__(self):
        self.Acoount_holder_name = ''
        self.phone_number = 0
        self.address = ''
        self.pin = 0
        self.balance = 0

        self.menu()

    def menu(self):

        user_input = input('''
        
        This is Non GUI Banking System Please Read the Following Instruction and Operate IT !
        
        
                              1. Enter 1 to Open Account
                              2. Enter 2 to Deposit
                              3. Enter 3 to WithDraw
                              4. Enter 4 to Check_Balance
                              5. Enter 5 to Change Pin
                              6. Enter 6 to Check_Account_Detail
                              7. Enter 7 to Get Pin
        ''')

        if user_input == '1':
            self.open_account()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.with_draw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            self.change_pin()
        elif user_input == '6':
            self.account_detail()
        elif user_input == '7':
            self.get_pin()
        else:
            print('Programme End')
            print('Thank You For Exploring')

    def open_account(self):
        print('~~~~~~~~~~~~~~~Open Account~~~~~~~~~~~~~~~')
        self.Acoount_holder_name = input('Enter Your Name : ')
        self.phone_number = int(input('Enter a Phone Number : '))
        self.address = input('Enter Your Address : ')
        self.pin = int(input('Create Your Pin : '))
        print('Account Open SucessFully ! ')

        self.menu()

    def account_detail(self):
        print('~~~~~~~~~~~~~~~Acoount Details~~~~~~~~~~~~~~~')
        user = int(input('Enter Your Pin : '))
        if user == self.pin:
            print('Account Holder Name : ', self.Acoount_holder_name)
            print('Phone Number : ', self.phone_number)
            print('Address : ', self.address)
            print('Current_Amount : ', self.balance)
            print('Cuurent_Pin : ', self.pin)
        else:
            print('Invalid Pin')
        self.menu()

    def deposit(self):
        print('~~~~~~~~~~~~~~~Deposit~~~~~~~~~~~~~~~')
        user = int(input('Enter Your Pin : '))
        if user == self.pin:
            amount = int(input('Enter a Amount : '))
            self.balance = self.balance + amount
            print('Deposit sucessfully')
        else:
            print('Invalid')
        self.menu()

    def with_draw(self):
        print('~~~~~~~~~~~~~~~WithDraw Cash~~~~~~~~~~~~~~~')
        user = int(input('Enter Pin : '))
        if user == self.pin:
            amount = int(input('Enter a Amount : '))
            self.balance = self.balance - amount
            print('Withdraw Sucessfuly ')
        else:
            print('Insufficient Amount')
        self.menu()

    def check_balance(self):
        print('~~~~~~~~~~~~~~~Check Balance~~~~~~~~~~~~~~~')
        user = int(input('Enter a Pin : '))
        if user == self.pin:
            print('Current_Ammount : ', self.balance)
        else:
            print('Invalid')
        self.menu()

    def change_pin(self):
        print('~~~~~~~~~~~~~~~Changing Pin~~~~~~~~~~~~~~~')
        new_pin = int(input('Create new Pin : '))
        if type(new_pin) == int:
            self.pin = new_pin
            print('Pin Create Sucessfully')
        else:
            print('Not Allowed')
        self.menu()

    def get_pin(self):
        print('~~~~~~~~~~~~~~~Getting Pin~~~~~~~~~~~~~~~')
        print('Your Current_pin : ', self.pin)

        self.menu()


sbi = Bank()

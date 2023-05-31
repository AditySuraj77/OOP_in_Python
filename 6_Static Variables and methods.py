class Atm:

    __counter = 0  # Static/Class variables

    def __init__(self):

        # Instance variables
        self.__pin = ''  # Hide
        self.__balance = 0  # Hide

        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        #elf.__menu()  # Hide


    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_conter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print('Not Allowed')


    def __menu(self):  # Hide

        user_input = input('''
                            Hello how would you like to proceed
                            1. Enter 1 Create Pin
                            2. Enter 2 to Deposit
                            3. Enter 3 to WithDraw
                            4. Enter 4 to Check Balance
                            5. Enter 5 to Get Pin
                            6. Enter 6 to Exit
            ''')

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            self.get_pin()
        else:
            print('Exit')

    def create_pin(self):
        print('Create Pin')
        self.__pin = input('Enter Your pin : ')  # Hide
        print('Pin Set Sucessfully')
        self.__menu()  # Hide

    def deposit(self):
        print('Deposit your Amount')
        temp = input('Enter Pin : ')
        if temp == self.__pin:  # Hide
            amount = int(input('Enter Amount : '))
            self.__balance = self.__balance + amount  # Hide,   # 2nd method self.balance += amount
        else:
            print('Invalid PIn')
        self.__menu()  # Hide

    def withdraw(self):
        print('Withdraw your amount')
        temp = input('Enter Pin : ')
        if temp == self.__pin:  # Hide
            amount = int(input('Enter Amount : '))
            if amount < self.__balance:  # Hide
                self.__balance = self.__balance - amount  # Hide,  ## 2nd method self.balance -= amount
                print('WithDraw Sucessfully')
            else:
                print('Insufficient Amount')
        else:
            print('Invalid Pin')
        self.__menu()  # Hide

    def check_balance(self):
        print('Check Balance')
        temp = input('Enter Pin : ')
        if temp == self.__pin:  # Hide
            print(self.__balance)  # Hide
        else:
            print('Invalid Pin')
        self.__menu()  # Hide

    def get_pin(self):   # Getter
        print(self.__pin)
        self.__menu()

    def set_pin(self, new_pin):  #Setter
        if type(new_pin) == int:
            self.__pin = new_pin
            print('New Pin Set SucessFully')
        else:
            print('Not Allowed')
        self.__menu()  # Hide
#o1 = Atm()

#print(o1.counter)

#o2 = Atm()
#print(o2.counter)

#o3 = Atm()
#print(o3.counter)

#o4 = Atm()
#print(o4.counter)

#print(Atm.counter)

print(Atm.get_counter())  #Fetching a counter no

print(Atm.set_conter(5)) # Set a Counter no 5

print(Atm.get_counter()) # Again Fetching Counter no
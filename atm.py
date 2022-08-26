class Atm:

    def __init__(self):
        #print("Hello")
        self.__pin=""  # (__pin )underscore : this will make the pin private
        self.__balance=0

        self.__menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("pin changed")

    def __menu(self):
        user_input = input("""
            enetr 1 to enter pin
            enter 2 to deposit
            enter 3 to wdr
            enter 4 to check balance
            enter 5 to exit
""")

        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.wdr()
        elif user_input=="4":
            self.check_bal()
        elif user_input=="5":
            self.exit()
            #print("bye")    

    def create_pin(self):
        self.__pin =input("Enter pin : ")
        print("Pin set succesful")
        #self.__menu()

    def deposit(self):
        temp = input("enter your pin : ")
        if temp == self.__pin:
            amount=int(input("eneter the amount to depost : "))
            self.__balance = self.__balance+amount
            print("account bal is : "+ str(self.__balance))
        else:
            print("Invalid pin")
        #self.__menu()

    def wdr(self):
        temp =input("enter your pin : ")
        if temp == self.__pin:
            amount=int(input("eneter the amount to withdraw : "))
            if amount <= self.__balance:
                self.__balance = self.__balance-amount
                print("remaining amount is : "+ str(self.__balance))
            else:
                print("insufficient amount")
        else:
            print("Invalid pin")
        #self.__menu()    

    def check_bal(self):
        pin = input("enter the pin to check balance : ")
        if self.__pin == pin:
            print("your account balance is : "+ str(self.__balance))
        else:
            print("Wrong pin")
        #self.__menu()

    def exit(self):
        #self.exit=input("Enter 5 to exit : ")
        print("bye tc, have a good day!!")
        #self.__menu()


        


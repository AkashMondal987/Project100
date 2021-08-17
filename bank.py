class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
    
    def checkBalance(self):
        print("Your Balance Is 10,000")

    def withdrawl(self,amount):
        newAmount = 10000 - amount
        print("You Have Withdrawhed: "+str(amount)+"  Your Remaining Balance Is: "+str(newAmount))

    def main():
        cardNumber = input("Enter Your Card Number: ")
        pin = input("Enter Your Pin: ")
        newUser = Atm(cardNumber,pin)

        print("Choose What You Want To Do...")
        print("1. Balance 2.Withdraw")

        activity = int(input("Enter The Number: "))

        if(activity == 1):
            newUser.checkBalance()
        elif(activity == 2):
            amount = int(input("Enter The Amount: "))
            newUser.withdrawl(amount)
        else:
            print("Enter A Valid Number: ")

Atm.main()
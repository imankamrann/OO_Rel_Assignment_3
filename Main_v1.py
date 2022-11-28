from Logic_v1 import Account, SavingAccount, ChecquingAccount, Bank


class Program:
    def run(self):
        self.showMainMenu()

    def showMainMenu(self):
        print("\n\033[1;30;44mHello Welcome to the Bank! \033[0m\n")
        bank = Bank()

        while True:
            try:
                userInput = int(
                    input("\n\033[1;34;10mEnter Account # you would like to use (either 1,2,3,4,5): \033[0m"))
                acc = bank.searchAccount(userInput)
                if acc is not None:
                    self.showAccountMenu(acc)

            except:
                print("\n\033[1;31;10mIncorrect data entered \033[0m\n")

    def showAccountMenu(self, acc):

        while True:

            print("\n\033[1;30;44mWelcome to Account Menu, Choose From the Following Options: \033[0m\n")
            userChose = int(
                input("\n\033[1;34;10mCheck Balance [1] | Deposit Money [2] | Withdraw Money [3] | Quit [4] :  \033[0m"))

            if userChose == 1:
                print("\n\033[1;32;10mAccount balance: $", acc.getCurrentBalance(), "CAD\033[0m\n")
                

            elif userChose == 2:

                while True:
                    try:
                        userDeposit = int(input("\nEnter Deposit Amount: $ "))
                        if userDeposit >= 1:
                            acc.deposit(userDeposit)
                            print("\n\033[1;32;10mNew Balance: $", acc.getCurrentBalance(), " CAD\033[0m\n")
                            break
                    except:
                        print("\n\033[1;31;10mIncorrect data entered. Try Again \033[0m")

            elif userChose == 3:
            
                while True:
                    try:
                        userWithdraw = int(input("\nEnter Withdrawl Amount: $"))
                        if acc.isValidWithdraw(userWithdraw):
                            acc.updateBal(userWithdraw)
                            print("\n\033[1;33;10mYou withdrew: $", userWithdraw , " CAD\033[0m")
                            print("\n\033[1;32;10mcurrent bal: $", acc.getCurrentBalance(), " CAD\033[0m\n")
                            break
                        else:
                            print("\n\033[1;31;10mA minimum bal of $1000 is required \033[0m")
                    except:
                        print("\n\033[1;31;10mIncorrect data entered. Try Again \033[0m")

            elif userChose == 4:
                #quit
                while True:
                    try:
                        userExit = input("\n\033[1;33;10mAre you sure you want to exit to main menu? y/n: \033[0m")
                        if userExit == 'y':
                            print("\nGoodbye!")
                            p.run()

                        elif userExit == 'n':
                            break

                        else:
                            print("\n\033[1;31;10mTo exit to main menu, please enter y/n: \033[0m")
                    except:
                        print("\n\033[1;31;10mIncorrect data entered. Try Again \033[0m")

            else:
                print("\n\033[1;31;10mIncorrect Value Entered. Try again. \033[0m")


p = Program()
p.run()

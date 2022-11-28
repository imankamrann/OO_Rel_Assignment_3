
class Account:
    def __init__(self, num, name, roi, balance):
        self._num = num
        self._name = name
        self._roi = roi
        self._balance = balance

    def getAccountNumber(self):
        return self._num

    def getAccountHolderName(self):
        return self._name

    def getRateOfInterest(self):
        return self._roi

    def getCurrentBalance(self):
        return self._balance
    
    def checkBalance(self):
        print("\n\033[1;33;10mAccount Balance: ", self._balance, " \033[0m")

    def deposit(self,amt):
        self._balance = self._balance + amt

    def withdraw(self):
        pass

    def showAccountsDetails(self):
        print("Account # -> ", self.getAccountNumber())
        print(f"Account Name -> {self.getAccountHolderName()}")
        print("Account Bal -> ", self.getCurrentBalance())
        print("Account ROI -> ", self.getRateOfInterest())


class SavingAccount(Account):
    def isValidWithdraw(self, amt):

        _minBal = 1000
      
        if((self._balance-amt) >= _minBal):
            return True
        else:
            return False

    def updateBal(self, userWithdraw):
        self._balance = self._balance - userWithdraw
        return self._balance

class ChecquingAccount(Account):

    def isValidWithdraw(self, amt):
        _overDraftAllowed = 2000

        if amt <= (self._balance + _overDraftAllowed):
            return True
        else:
            return False
       
    def updateBal(self, amt):
        self._balance = self._balance - amt
        return self._balance
       

class Bank:
    _bankName = None
    _listOfAcc = []

    def __init__(self):
       
        self._listOfAcc.append(SavingAccount(1, "Kaz", 1, 1500))
        self._listOfAcc.append(SavingAccount(2, "Inej", 2, 2000))
        self._listOfAcc.append(SavingAccount(3, "Nina", 3, 3000))
        self._listOfAcc.append(SavingAccount(4, "Jesper", 4, 4000))
        self._listOfAcc.append(SavingAccount(5, "Wylan", 5, 5000))
        
        #self.showAllAccounts()

    def searchAccount(self, userInput):
        for acc in self._listOfAcc:
            if acc.getAccountNumber() == userInput:
                print("\nAccount Number Found!")
                print("\nHi "+ acc.getAccountHolderName(),"!")
                return acc
        print("\n\033[1;31;10mAccount not Found. \033[0m")



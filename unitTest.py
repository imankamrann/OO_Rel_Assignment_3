from Logic import SavingAccount, ChecquingAccount

accList = []

a1 = SavingAccount(1,"A",5,1200)
a2 = ChecquingAccount(2,"B",6,2000)

# example of unit tests:

# print("account 1: ", a1.getAccountNumber())
# print("account 2: ", a2.getAccountNumber())

# accList.append(a1) 
# accList.append(a2)

# b = Bank()
# print(b.listOfAcc)

# b.searchAccount(1)

#print(a1.isValidWithdraw(100))

# print(a1.isValidWithdraw(500))
# print(a1.updateBal(1200))

print(a2.isValidWithdraw(1500))
print(a2.updateBal(2000))



import datetime
class Bank:
    bname = "sbi"  #static variable,to use memory efficiently.Here bname will be common for all object(person) so single memory space is enough for all object
    def createAccount(self,acno):
        #self.bname=bname hence we defined static variable above
        self.acno=acno
        self.balance=3000  #minimum balance should be 3000

    def deposite(self,amt):
        self.balance+=amt
        print("your ",self.bname,"account has been credited with amount", amt)
        print("on ",datetime.datetime.now(),"current balance =",self.balance)

    def withdraw(self,amt):
        if (amt>self.balance):
            print("insufficient fund")
        else:
            self.balance -= amt
        print("your ",self.bname,"account has been debited with amount", amt)
        print("on ",datetime.datetime.now(),"current balance =",self.balance)

    def balanceEnq(self):
        print("your account balance = ",self.balance)


obj=Bank()
obj.createAccount(1003)
obj.balanceEnq()
obj.deposite(200)
obj.withdraw(200)

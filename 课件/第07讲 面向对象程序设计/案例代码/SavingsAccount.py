"""
定义一个类SavingsAccount描述银行账户
ZhangHua @ 20190706
"""


class SavingsAccount:
    cm_AnnualInterestRate = 0.03

    @staticmethod
    def setAnnualInterstRate(rate):
        SavingsAccount.cm_AnnualInterestRate = rate

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    def deposit(self, money):
        if money>0:
            self.__balance += money

    def withdraw(self, money):
        if money>0 and money<self.__balance:
            self.__balance -= money

def printSavingsAccount(sa):
    print("Name:{}\nBalance:￥{}".format(sa.name, sa.balance))
    print("Annual Interest Rate:{}\nMonthly Interest:￥{:.3f}".format(
        sa.cm_AnnualInterestRate,
        sa.balance*sa.cm_AnnualInterestRate/12))

def test_SavingsAccount():
    a1 = SavingsAccount('LiTao', 2000)
    printSavingsAccount(a1)
    print()

    SavingsAccount.setAnnualInterstRate(0.025)
    printSavingsAccount(a1)
    print()

    a2 = SavingsAccount('WangHui', 10000)
    a2.deposit(3000)
    printSavingsAccount(a2)
    print()

    a2.withdraw(5000)
    printSavingsAccount(a2)


if __name__ == '__main__':
    test_SavingsAccount()
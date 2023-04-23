"""
    模拟两个银行帐户转帐死锁现场
"""

from time import sleep
from threading import  Thread,Lock


# 帐户类
class Account():
    def __init__(self,_id,balance,lock):
        # 用户id
        self.id = _id
        self.balance = balance
        self.lock = lock

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount

    # 存钱
    def deposit(self,amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance

# 产生两上帐户
tom = Account('tom',5000,Lock())
alex = Account('alex',8000,Lock())

# 转帐过程
def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount)
        sleep(1)
        if to.lock.acquire():
            to.deposit(amount)
            to.lock.release()
        # 出现死锁,问题在这样,由于from_locl.release解锁
        # 应该在from_.withdraw(amount) 转账完成后,立即解锁
        # 由于没有即时解锁,所以在执行to.lock.acquire():这里时,需要from_的资源,所以就出现了死锁
        from_.lock.release()
    print("%s给%s转帐%d"%(from_.id,to.id,amount))


t1 = Thread(target=transfer,args=(tom,alex,2000))
t2 = Thread(target=transfer,args=(alex,tom,3500))

t1.start()
t2.start()

t1.join()
t2.join()


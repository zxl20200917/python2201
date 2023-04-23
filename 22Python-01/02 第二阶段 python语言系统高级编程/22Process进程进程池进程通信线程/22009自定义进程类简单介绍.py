"""
    目前理解应用：
        可以在以后的项目中把多个进程多个功能，封装到一个自定义进程类中，通过调用自定义类进行功能的实现。
"""

from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        # 如果不想遗失Process类属性，需要把父类的init方法也添加进来
        # 调用父类属性，需要super
        super().__init__()

    # 简单定义方法fun1 fun2
    def fun1(self):
        print("工作步骤1")

    def fun2(self):
        print("工作步骤2")

    # 重写run方法
    def run(self):
        self.fun1()
        self.fun2()


def main():
    p = MyProcess(2)
    p.start()
    p.join()


if __name__ == '__main__':
    main()

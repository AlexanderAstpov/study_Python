class Money:
    def __init__(self, an_integer, fractoinal_num):
        self.an_integer = an_integer
        self.fractoinal_num = fractoinal_num

    def _an_integer(self):
        print(f"Баланс целой части счета = {self.an_integer}")

    def _fractoinal_num(self):
        print(f"Баланс дробной части счета = {self.fractoinal_num}")
    
    
    def show_balans(self):
        print(f"Ваш баланс = {self.an_integer}.{self.fractoinal_num}")


a = Money(10, 35)
a._an_integer()
a._fractoinal_num()
a.show_balans()

        


    
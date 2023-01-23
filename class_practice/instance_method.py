class Test:
    a = 10
    
    def __init__(self):
        self.b = 30

    def m1(self):
        self.a = 888
        Test.b = 999

t1 = Test()
t2 = Test()

t1.m1()
print("T1 : ",t1.a , t1.b)
print("T2 : ",t2.a , t2.b)
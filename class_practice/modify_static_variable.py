# static variable

class Test:
    a =10

    def __init__(self) -> None:
        Test.a=20

    def m1(self):
        Test.a = 30
    
    @classmethod
    def m2(cls):
        
        Test.a=50
        cls.a=40
    
    @staticmethod
    def m3():
        Test.a=60

t = Test()
t.m1()
t.m2()
Test.m3()
t.a=70
Test.a=80
print(Test.a)
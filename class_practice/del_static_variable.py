# delete static variable

class Test:
    #static variable
    a = 10

    @classmethod
    def del_static_variable(cls):
        # Two way two delete static variable
        del Test.a
        # del cls.a

"""Two way to call method"""  
# reference variable      
t = Test()
t.del_static_variable()

#by using class name
# Test.del_static_variable()
print(Test.__dict__)


class Number:
    a = 10

    def __init__(self) -> None:
        Number.b = 20
        del Number.a
    
    def m1(self):
        Number.c = 30
        del Number.b
    
    @classmethod
    def m2(cls):
        cls.d = 40
        del Number.c
    
    @staticmethod
    def m3():
        Test.e = 50
        del Number.d

# Note :- never delete object to delete static variable like (del n.a) --> it's show Attribute error
n = Number()
Number.m1(n)
Number.m2()
n.m3()
print(Test.__dict__)
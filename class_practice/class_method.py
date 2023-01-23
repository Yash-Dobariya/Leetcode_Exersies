# Class method

class Test:
    count = 0

    def __init__(self) -> None:
        Test.count = Test.count + 1

    @classmethod
    def getNoOfObject(cls):
        print("The number of object : ",cls.count)
    

t1 = Test()
t1 = Test()
t1 = Test()
t1 = Test()

Test.getNoOfObject()
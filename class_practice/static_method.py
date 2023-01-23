# static method

class calculate:
    a=10
    @staticmethod
    def sum(a,b):
        print( "Sum : ",a + b)
    
    # @staticmethod
    def mul(a,b):
        return "multiplication : ",a * b
    
    @staticmethod
    def div(a,b):
        return "Division : ",a / b

    @staticmethod
    def sub(a,b):
        return "Substraction : ",a - b

c=calculate()
print(calculate.mul(10,20))
# calculate.mul(10,20)

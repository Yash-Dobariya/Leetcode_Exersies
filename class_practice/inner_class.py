class Outer:

    def __init__(self) -> None:
        print("Outer class")

    class Inner:

        def __init__(self) -> None:
            print("Inner class")

        def m1(self):
            print("Inner classs method")

# first method to call inner class
t= Outer()
i=t.Inner()
i.m1()
print("\'Secound method \'")
# secound method to call inner class
i=Outer().Inner()
i.m1()
print("\'Third method \'")
i=Outer().Inner().m1()
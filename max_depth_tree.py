class Node:

    def __init__(self,data):
        self.right= None
        self.left=None
        self.data=data

    def insert(self,data):
        if self.data is None:
            self.data= data
        else:
            if data<self.data and self.left != None:
                self.left.insert(data)
                
            elif data>self.data and self.right != None:
                self.right.insert(data)

            return data

root=Node (1)
print(root.insert(100))
print(root.insert(200))
print(root.insert(150))
print(root.insert(7))
print(root.left.data)
class Node:

    def __init__(self,data):
        self.data=data
        self.left= None
        self.right=None

# data=[3,9,20,15,7]
n1=Node(3)
n2=Node(9)
n3=Node(20)
n4=Node(15)
n5=Node(7)



n1.left=n2
print(n1.left.data)
n2.left=n3
print(n2.left.data)
n3.left=n4
print(n3.left.data)
n1.right=n5
print(n1.right.data)

data=n1,n2,n3,n4,n5

if data==None:
    pass
while data >0:
    if data.left != None:
        max_left=max(data.left)
    
    elif data.right != None:
        max_right=max(data.right)

    print(max(max_left,max_right))
    
        # if data == None:
        #     return None

        # if self.data ==None:
        #     return data+1

# print(data)

# n1.left=n2
# print(n1.left.data)

# n1.right=n3
# print(n1.right.data)

# n2.left=n4
# print(n2.left.data)

# n2.right=n5
# print(n2.right.data)

# n3.left=n6
# print(n3.left.data)

# n5.left=n7
# print(n5.left.data)

# n5.right=n8
# print(n5.right.data)

# print("**************************")
# for i in range(n8.data):
#     max
#     print(i)
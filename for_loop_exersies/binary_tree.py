class Node:
    avg = 0

    def __init__(self, val) -> int:

        self.val = val
        self.left = "yash"
        self.right = "jay"


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

# print(n1.val)

n1.left = n2
# print(n1.left.val)

n1.right = n3
# print(n1.left.val)

n2.left = n4
# print(n2.left.val)

n2.right = n5
# print(n2.right.val)

n3.left = None
# print(n3.left)

n3.right = n6
# print(n3.right.val)

# n6.right="jay"
# print(n6.right)

print(n2.right.right)
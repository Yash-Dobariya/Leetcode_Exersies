# Linked list

class Linkedlist:

    head = [3, 2, 0, -4]
    pos = 1

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


n1 = Linkedlist(3)
n2 = Linkedlist(2)
n3 = Linkedlist(0)
n4 = Linkedlist(-4)

n1.next = n2.data
n2.next = n3.data
n3.next = n4.data
n4.next = n2.data

head = []
slow = fast = head
for i in n1.data,n1.next, n2.next, n3.next :
    head.append(i)

    while fast == slow:
        slow= slow.next
        fast= fast.next
if fast==slow:
    print(True)
# else:
    print(False)
print(head)


# slow = fast = head

# while fast and slow :
# fast = fast.next
# slow = slow.next

# if fast == slow:
# print("True")
#     else :
# print("False")


# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n2

# pos=2

# list1=[]
# list1.append(n1.data)
# list1.append(n2.data)
# list1.append(n3.data)
# list1.append(n4.data)
# print(list1)

# while list1:
#     list1.append()


# if pos==n2 :
#     print("True")
# else:
#     print("False")

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head=ListNode(0)
# for i in range():
n1=ListNode(1)
n2=ListNode(2)

head.next=n1
head.next.next=n2

class Solution:
    def rotateRight(self, head, k: int):
        for i in range(k):
        
            a=head.pop()
            head.insert(0,a)

        print(head)
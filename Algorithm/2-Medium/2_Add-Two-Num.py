# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a dummy node for reference
        dummynode= ListNode(0)
        current=dummynode
        carry=0

        while l1!= None or l2 != None or carry !=0:
            # Checking if a node exists in the list
            l1value = l1.val if l1 else 0
            l2value = l2.val if l2 else 0
            sum= l1value+l2value+carry
            carry = sum //10 # Adding quotient value to carry
            current.next=  ListNode(sum%10) # Adding remainder value to the node
            # Updating list node pointers
            current= current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummynode.next 
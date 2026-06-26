# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next
        #self.head = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current  = head
        nextnode = None
        while(current is not None):
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        return prev



    

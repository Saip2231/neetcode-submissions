# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = head
        current = head
        count = 1
        diff = 1
        while(index.next is not None):
            index = index.next
            count = count + 1
        while(diff < (count - n)):
            current = current.next
            diff = diff +1
        print(count , n)
        if(count - n == 0):
            return (head.next)
        else:
            temp = current.next
        # print(current.val , current.next.val)
        # print(temp.val , temp.next.val)
            current.next = temp.next
        return head
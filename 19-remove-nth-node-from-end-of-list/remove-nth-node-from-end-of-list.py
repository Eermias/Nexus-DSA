# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        # first find the lenght
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return None
        
        index = length - n
        # start from the first element and find the desired node
        curr = head
        prev = dummy
        for i in range(index):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return dummy.next

        
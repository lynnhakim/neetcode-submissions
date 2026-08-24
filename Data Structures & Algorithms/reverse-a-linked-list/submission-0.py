# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
[0,1,2,3]
 h
temp = h -> nh = 

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        while head:
            temp = ListNode(head.val, newHead)
            newHead = temp
            head = head.next
        return newHead
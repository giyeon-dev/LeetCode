# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        curr = dummyNode 
        num = 0

        while l1 or l2 or num:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sm = val1 + val2 + num
            num = sm // 10
            digit = sm % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummyNode.next
        
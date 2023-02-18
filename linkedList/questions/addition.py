# Definition for singly-linked list.
# pyright: reportOptionalMemberAccess=false
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val is None and l2.val is None:
            return None
        elif l1.val is None:
            return l2
        elif l2.val is None:
            return l1
        
        result = ListNode()

        carry = False
        sum = 0

        while l1 or l2:
            sum = l1.val + l2.val
            if carry:
                sum += 1

            carry = False

            if sum >= 10:
                carry = True
                sum = sum / 10

            newNode = ListNode(sum)

            itr = result
            while itr.next:
                itr = itr.next
            itr.next = newNode

            # update the iterators
            l1 = l1.next
            l2 = l2.next

        return result

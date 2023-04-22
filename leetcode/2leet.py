# https://leetcode.cn/problems/add-two-numbers/description/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = 0
        cur = head = ListNode(0)
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + t
            tmp = sum % 10
            t = sum // 10
            cur.next = ListNode(tmp)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if t > 0:
            cur.next = ListNode(t)
        return head.next






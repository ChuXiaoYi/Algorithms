# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/2/28 下午2:58
#       @Author  : cxy =.= 
#       @File    : 21demo.py
#       @Software: PyCharm
#       @Desc    : 21. 合并两个有序链表 https://leetcode-cn.com/problems/merge-two-sorted-lists/
# ---------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return ListNode(None)

        result = ListNode(0)

        if l1.val <= l2.val:
            result = ListNode(l1.val)
            l1 = l1.next
        elif l1.val > l2.val:
            result = ListNode(l2.val)
            l2 = l2.next

        res = result

        while l1 and l2:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                result.next = ListNode(l2.val)
                l2 = l2.next
            result = result.next

        if l1:
            result.next = l1
        elif l2:
            result.next = l2
        return res






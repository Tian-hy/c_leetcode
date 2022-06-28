#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cur1 = l1
        cur2 = l2

        n = 1
        while cur1:
            num1 += cur1.val * n
            n *= 10
            cur1 = cur1.next

        n = 1
        while cur2:
            num2 += cur2.val * n
            n *= 10
            cur2 = cur2.next
        
        num = num1 + num2

        head = ListNode(None, None)
        cur = head
        while num > 9:
            cur.next = ListNode(num % 10, None)
            num = num // 10
            cur = cur.next
        cur.next = ListNode(num, None)
        return head.next
# @lc code=end


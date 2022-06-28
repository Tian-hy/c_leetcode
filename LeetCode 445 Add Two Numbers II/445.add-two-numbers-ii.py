#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
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

        while l1:
            num1 = l1.val + num1 * 10
            l1 = l1.next

        num2 = 0

        while l2:
            num2 = l2.val + num2 * 10
            l2 = l2.next
        
        num = num1 + num2
        print(num, num1, num2)
        head = ListNode(None, None)
        cur = head
        for item in str(num):
            cur.next = ListNode(item)
            cur = cur.next

        return head.next

# @lc code=end


#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def show(self, h):
        while h:
            print(h.val, end=" ")
            h = h.next
        print(" ")

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        pre, slow, fast = ListNode(None, None), head, head
        while fast and fast.next:
            print(pre.val, slow.val, fast.val)
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
# @lc code=end


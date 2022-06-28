#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        idx = 1
        pre_l = ListNode(None, None)
        cur = head
        while idx != left:
            pre_l = cur
            cur = cur.next
            idx += 1

        pre, l = cur, cur
        
        while idx-1 != right:
            idx += 1
            if cur is None:
                break
            next = cur.next
            pre_l.next = cur
            cur.next = pre
            pre = cur
            cur = next
        l.next = cur
        return  pre_l.next if pre_l.val is None else head
        
# @lc code=end


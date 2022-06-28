#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        lower = ListNode(None, None)
        lower_head = lower
        upper = ListNode(None, None)
        upper_head = upper
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = None
            if cur.val < x:
                lower.next = cur
                lower = lower.next
            else:
                upper.next = cur
                upper = upper.next
            cur = next
        if lower_head.next is None and upper_head.next is not None:
            return upper_head.next
        elif upper_head.next is None and lower_head.next is not None:
            return lower_head.next
        elif lower_head.next and upper_head.next:
            lower.next = upper_head.next
            return lower_head.next

# @lc code=end


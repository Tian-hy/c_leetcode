#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        
        pre = ListNode(None, head)
        slow = fast = head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        if fast is not None:
            pre, slow = slow, slow.next
        pre.next = None

        # reverse
        slow_n= slow.next
        slow.next = None
        while slow_n:
            slow_nn = slow_n.next
            slow_n.next = slow
            slow = slow_n
            slow_n = slow_nn

        # merge
        cur = dummy_head = ListNode(None)
        idx = 1
        while head or slow:
            if idx % 2:
                cur.next = head
                head = head.next
            else:
                cur.next = slow
                slow = slow.next
            cur = cur.next
            idx += 1
        
        return dummy_head.next
        
# @lc code=end


#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        pre = dummy_head

        while pre.next and pre.next.next:
            l, r = pre.next, pre.next.next
            next = r.next

            pre.next = r
            r.next = l
            l.next = next

            pre = l
        return dummy_head.next
        
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy_head = ListNode(None, head)
        pre = dummy_head
        l = head
        r = head.next
        cur = head.next
        while cur:
            next = cur.next
            if l and r is None:
                r = cur
                r.next = None
            elif l is None and r is None:
                l = cur
                l.next = None
            if r:
                pre.next = r
                r.next = l
                l.next = None
                pre = l
                l, r = None, None
            cur = next
        if l and r:
            pre.next = r
            r.next = l
            l.next = None
        elif l and r is None:
            pre.next = l
            l.next = None
        return dummy_head.next
# @lc code=end


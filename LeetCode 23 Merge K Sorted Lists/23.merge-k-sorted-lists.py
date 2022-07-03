#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l, r):
            dummy = cur = ListNode(None, None)
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            if l is None and r:
                cur.next = r
            elif r is None and l:
                cur.next = l
            return dummy.next

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        length = len(lists)
        l = lists[0]
        for i in range(1, length):
            l = merge(l, lists[i])
        return l
# @lc code=end


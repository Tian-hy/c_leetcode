#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = ListNode(None, None)
        cur = head

        while cur is not None:
            next = cur.next
            if pre.val == cur.val:
                pre.next = next
                cur = next
            else:
                pre = cur
                cur = next
        return head
        
# @lc code=end


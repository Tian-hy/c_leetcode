#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        pre = dummy_head
        cur = head
        duplicate_set = set()

        while cur:
            if cur.val in duplicate_set or (cur.next and cur.val == cur.next.val):
                duplicate_set.add(cur.val)
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return dummy_head.next
        
# @lc code=end


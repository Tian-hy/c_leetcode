#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        idx = 2
        odd = head
        even = odd.next
        even_head = even
        cur = even.next
        even.next = None

        while cur:
            idx += 1
            next = cur.next
            cur.next = None
            if idx % 2 == 0:
                even.next = cur
                even = even.next
            else:
                odd.next = cur
                odd = odd.next
            cur = next
        
        odd.next = even_head

        return head
        
# @lc code=end


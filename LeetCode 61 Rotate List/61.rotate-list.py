#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        k = k % length
        
        if k == 0:
            return head 

        dummy_head = ListNode(None, head)
        p = q = dummy_head
        while k+1:
            q = q.next
            k -= 1
        
        while q:
            p = p.next
            pre_q = q
            q = q.next
        
        p_next = p.next
        p.next = None
        pre_q.next = dummy_head.next
        dummy_head.next = p_next
        return dummy_head.next


        
# @lc code=end


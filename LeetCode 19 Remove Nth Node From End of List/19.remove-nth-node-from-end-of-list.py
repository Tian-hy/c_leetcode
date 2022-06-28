#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    head = 1 2 3 4 5 None, n = 2
        p     q
    1 2 3 4 5 None
    the dis between p and q is constant

    p     q
    1 2 3 4 5 None
      p     q
    1 2 3 4 5 None
        p     q
    1 2 3 4 5 None
    p.next = p.next.next
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        p = q = dummy_head
        while n+1:
            q = q.next
            n -= 1
        
        while q:
            p = p.next
            q = q.next
        
        p.next = p.next.next

        return dummy_head.next
# @lc code=end


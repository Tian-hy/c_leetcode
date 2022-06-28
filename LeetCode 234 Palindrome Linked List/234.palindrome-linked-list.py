#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return head

        pre = ListNode(None, head)
        slow = fast = head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        if fast is not None:
            slow = slow.next
        slow_n = slow.next
        slow.next = None

        while slow_n:
            slow_nn = slow_n.next
            slow_n.next = slow
            slow, slow_n = slow_n, slow_nn
        
        while slow:
            if slow.val != head.val:
                return False
            slow, head = slow.next, head.next

        return True

        
# @lc code=end


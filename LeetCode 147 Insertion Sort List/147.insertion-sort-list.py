#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def show(self, h):
        while h:
            print(h.val, end=" ")
            h = h.next
        print(" ")

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy_header = ListNode(None, head)
        cur = head
        maximum = head

        while cur:
            h = dummy_header
            next = cur.next

            while h.next != cur:
                if h.next.val > cur.val:
                    h_next = h.next
                    h.next = cur
                    cur.next = h_next
                    break
                h = h.next
            if cur.val >= maximum.val:
                maximum = cur
            maximum.next = next
            cur = next
        

        return dummy_header.next

# @lc code=end
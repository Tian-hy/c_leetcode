#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isTrue(self, pre, k):
        for i in range(k):
            if pre.next is None:
                return False
            pre = pre.next
        return True

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        pre = dummy_head

        while self.isTrue(pre, k):
            tmp =[]
            tmp_pre = pre
            for i in range(k):
                tmp_pre = tmp_pre.next
                tmp.append(tmp_pre)
            next = tmp_pre.next
            tmp_pre = pre
            while tmp:
                tmp_pre.next = tmp.pop()
                tmp_pre = tmp_pre.next
            pre = tmp_pre
            pre.next = next
        return dummy_head.next
# @lc code=end


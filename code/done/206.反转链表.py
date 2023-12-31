#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        """
        return self.reverse(None, head)

    def reverse(self, pre: ListNode, cur: ListNode) -> ListNode:
        if cur is None:
            return pre
        next = cur.next
        cur.next = pre
        return self.reverse(cur, next)


# @lc code=end

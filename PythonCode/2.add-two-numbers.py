#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=l1
        n2=l2
        out=ListNode(0)
        n3=out
        remain=0
        while n1 or n2:
            if n1 and n2:
                n3.next=ListNode(remain+n1.val+n2.val)
            else:
                n3.next=ListNode(remain+n1.val if n1 else remain+n2.val)
            if n3.next.val>=10:
                n3.next.val-=10
                remain=1
            else:
                remain=0
            if n1:n1=n1.next
            if n2:n2=n2.next
            n3=n3.next
        if remain:
            n3.next=ListNode(1)
        return out.next

# @lc code=end


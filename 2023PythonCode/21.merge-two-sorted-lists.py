#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        res = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                sentinel.next = ListNode(list1.val)
                list1 = list1.next
            else:
                sentinel.next = ListNode(list2.val)
                list2 = list2.next
            sentinel = sentinel.next
        if not list1:
            sentinel.next = list2
        if not list2:
            sentinel.next = list1
        return res.next
# @lc code=end


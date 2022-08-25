#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        if head.next == None:
            return head
        '''
        
        prev = None
        cur = head
        while cur:
            prev = ListNode(cur.val, prev)
            cur = cur.next
        return prev

        
# @lc code=end


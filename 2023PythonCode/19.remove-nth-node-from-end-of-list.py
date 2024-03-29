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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        cpList = []
        while head != None:
            cpList.append(head.val)
            head = head.next
        cpList.pop(-n)
        sentinel = ListNode()
        res = sentinel
        for i in cpList:
            sentinel.next = ListNode(val = i)
            sentinel = sentinel.next
        return res.next
        '''
        # Can using fast-slow pointer
        sentinel = ListNode(0, head)
        fastPointer = head
        slowPointer = sentinel
        for _ in range(n):
            fastPointer = fastPointer.next
        while fastPointer:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next
        slowPointer.next = slowPointer.next.next
        return sentinel.next

        
# @lc code=end


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
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    #Using sentinel node
    l3 = ListNode(0)
    sentinel = l3
    remain = 0
    while l1 or l2:
        nextDigit = l1.val + l2.val + remain
        if nextDigit >= 10:
            nextDigit -= 10
            remain = 1
        else: 
            remain = 0
        l3.next = ListNode(nextDigit)
        l1 = l1.next
        l2 = l2.next
        l3 = l3.next
    if not l1: l3.next = l2
    elif not l2: l3.next = l1
    return sentinel.next

L1 = ListNode(2, ListNode(4, ListNode(3)))   
L2 = ListNode(5, ListNode(6, ListNode(4)))
L3 = ListNode(9, ListNode(9))
L4 = ListNode(9)
L5 = None
addTwoNumbers(L3, L4)
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Using sentinel node
        if not l1: return l2
        if not l2: return l1
        l3 = ListNode(0)
        sentinel = l3
        remain = 0
        while l1 or l2:
            if l1 and l2:
                l3.next = ListNode(l1.val + l2.val + remain)
            else:
                l3.next = ListNode(l1.val + remain if l1 else l2.val + remain)
            if l3.next.val >= 10:
                l3.next.val -= 10
                remain = 1
            else: 
                remain = 0
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            l3 = l3.next
        #In case sum of two lists still remain 1 for example 99 + 9
        if remain:
            l3.next = ListNode(1)
        return sentinel.next
        #Using sentinel node

# @lc code=end


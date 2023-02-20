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
        if list1==None:
            return list2
        elif list2 == None:
            return list1
        else:
            ptr0 = ListNode()
            head = ptr0
            ptr1 = list1
            ptr2 = list2
            while (ptr1 and ptr2):
                if ptr1.val > ptr2.val:
                    ptr0.next = ptr2
                    ptr0 = ptr0.next
                    ptr2 = ptr2.next
                else:
                    ptr0.next = ptr1
                    ptr0 = ptr0.next
                    ptr1 = ptr1.next

        if ptr1==None:
            ptr0.next = ptr2
            return head.next
        elif ptr2 == None:
            ptr0.next = ptr1
            return head.next
            



        
# @lc code=end


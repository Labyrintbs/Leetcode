#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def merge2Lists(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.merge2Lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge2Lists(list1, list2.next)
            return list2
    '''
    def merge2Lists(self,l1,l2):
        if not l1:
            return l2
        elif not l2 : 
            return l1
        elif l1.val < l2.next:
            l1.next = self.merge2Lists(l1.next,l2)
            return l1
        else:
            l2.next = self.merge2Lists(l1,l2.next)
            return l2 
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''fuck iteration
        n = len(lists)
        max_interval = 1
        #change : interval_len(/2), limit: interval_num = 1
        while max_interval < n:
            for i in range(0,n-max_interval,2*max_interval):
                lists[i] = self.merge2Lists(lists[i],lists[i+max_interval])
                max_interval *= 2 
        '''
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            l , r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
            return self.merge2Lists(l,r)
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
    






        
# @lc code=end


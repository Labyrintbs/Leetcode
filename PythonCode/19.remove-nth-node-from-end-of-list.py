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

from typing import List


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_head = ListNode(0,head)
        prev_head = ListNode(0,head)
        for i in range(n):
            cur_head = cur_head.next
            if cur_head.next == None:
                return head.next
        while cur_head.next != None:
            cur_head = cur_head.next
            prev_head = prev_head.next
        prev_head.next = prev_head.next.next
        return head
        '''
        cp_head = ListNode(0)
        cp_head.val = head.val
        cp_head.next = head.next
        dict_head = []
        l = 0
        while cp_head != None:
            dict_head.append(ListNode())
            dict_head[l].next = cp_head
            l+=1
            cp_head = cp_head.next
        l -=1
        dict_head[l+2-n].next.next = dict_head[l-n].next
        return head
        '''
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def removeNthFromEnd(head, n):
    cp_head = ListNode(0)
    cp_head.val = head.val
    cp_head.next = head.next
    dict_head = []
    l = 0
    while cp_head != None:
        dict_head.append(ListNode())
        dict_head[l].next = cp_head
        l+=1
        cp_head = cp_head.next
    l-=1
    dict_head[l+2-n].next.next = dict_head[l+1-n].next.next

node0 = ListNode(1)
node1 = ListNode(2,node0)
node2 = ListNode(3,node1)
node3 = ListNode(4,node2)
node4 = ListNode(5,node3)

removeNthFromEnd(node4,2)
'''
# @lc code=end


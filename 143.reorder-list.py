#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:return
        vec = []
        temp = head
        while temp:
            vec.append(temp)
            temp = temp.next
        n = len(vec) #sum equals to index 0 + index n = length -1
        i, j = 0 ,n-1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        
        vec[i].next = None


        
# @lc code=end


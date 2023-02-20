#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
node4 = TreeNode(8)
node3 = TreeNode(15)
node4 = TreeNode(7)
node1 = TreeNode(9,node4)
node2 = TreeNode(20,node3,node4)
node0 = TreeNode(3,node1,node2)
def levelOrder(root):
    res = []
    if not root:
        return res
    q = [root]
    while q :
        res.append([node.val for node in q])
        child = []
        for member in q:
            if member.left:
                child.append(member.left)
            if member.right:
                child.append(member.right)
        q = child
    return res
levelOrder(node0)
'''


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [root]
        while q :
            res.append([node.val for node in q])
            child = []
            for member in q:
                if member.left:
                    child.append(member.left)
                if member.right:
                    child.append(member.right)
            q = child

        return res


        
# @lc code=end


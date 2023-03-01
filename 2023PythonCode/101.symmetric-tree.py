#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # can't consider situation [1, 2, 2, 2, null, 2]
        '''
        res = []
        def preorder(root):
            if not root:
                return
            preorder(root.left)
            res.append(root.val)
            preorder(root.right)
        preorder(root)
        return res == res[::-1]
        '''
        def isSymmetricHelper(left, right):
            if not left and not right: return True

            elif not left or not right: return False

            elif left.val != right.val: return False

            else:
                return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
        if not root: return True

        if not root.left and not root.right: return True
        elif not root.left or not root.right: return False

        return isSymmetricHelper(root.left, root.right)
        
# @lc code=end


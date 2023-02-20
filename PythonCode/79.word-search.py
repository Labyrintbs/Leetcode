#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(i, j, mark, board, word):
            if len(word) == 0:
                return True
            
            directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direct in directs:
                cur_i = i + direct[0]
                cur_j = j + direct[1]
                
                if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                    # 如果是已经使用过的元素，忽略
                    if mark[cur_i][cur_j] == 1:
                        continue
                    # 将该元素标记为已使用
                    mark[cur_i][cur_j] = 1
                    if backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                        return True
                    else:
                        # 回溯
                        mark[cur_i][cur_j] = 0
            return False
    
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mark[i][j] = 1
                    if backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False
        
        


# @lc code=end


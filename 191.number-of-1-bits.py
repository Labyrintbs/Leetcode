#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        total = 0
        for i in range(32):
            last_bit = n & 1
            if last_bit:
                total += 1
            n >>= 1
        return total
        '''
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
        
# @lc code=end


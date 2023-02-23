#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}
        res = []
        n = len(digits)
        
        def backtrack(combination, index):
            if index == n:
                res.append(''.join(combination))
                return
            digit = digits[index]
            for letter in phone[digit]:
                combination.append(letter)
                backtrack(combination, index + 1)
                combination.pop()
        
        if n > 0:
            backtrack([], 0)
        
        return res
        '''
        def backtrack(combination, start_index):
            if start_index == n:
                res.append(''.join(combination))
                return
            for i in digits[start_index:]:
                for letter in phone[i]:
                    combination.append(letter)
                    backtrack(combination, start_index + 1)
                    combination.pop()
        
        if n > 0:
            backtrack([], 0)
            
        return res
        '''

'''
def letterCombinations(digits):
    phone = {'2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']}
    res = []
    n = len(digits)
    
    def backtrack(combination, index):
        if index == n:
            res.append(''.join(combination))
            return
        digit = digits[index]
        for letter in phone[digit]:
            combination.append(letter)
            backtrack(combination, index + 1)
            combination.pop()
    
    if n > 0:
        backtrack([], 0)
        
    return res

letterCombinations("23")
'''
        
# @lc code=end


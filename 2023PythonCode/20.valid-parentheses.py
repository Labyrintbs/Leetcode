#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # tedious if, can't solve pop from empty stack
        '''
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif i in (')', '}', ']'):
                if i == ')':
                    if stack.pop() != '(':
                        return False
                elif i == '}':
                    if stack.pop() != '{':
                        return False
                else:
                    if stack.pop() != '[':
                        return False 
        return stack == []
        '''
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1


        
# @lc code=end


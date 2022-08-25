#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


#from inspect import stack
'''
def isValid(s):
    stack = []
    for i in s:
        if i =='(' or i =='[' or i == '{':
            stack.append(i)
        elif stack == []:
            return False
        elif i == ')':
            if stack[-1] != '(':        
                return False
            else:
                stack.pop()
        elif i == ']':
            if stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif i == '}':
            if stack[-1] != '{':
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False

isValid("([)]")
'''
class Solution:
    def isValid(self, s: str) -> bool:

        
        stack = []
        for i in s:
            if i =='(' or i =='[' or i == '{':
                stack.append(i)
            elif stack == []:
                return False
            elif i == ')':
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif i == ']':
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        if stack == []:
            return True
        else:
            return False


        
# @lc code=end


#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
'''
def groupAnagrams(strs):
    d = {}
    for s in strs:
        s_sorted = "".join(sorted(s))
        if not s in d.keys():
            d[s_sorted] = [s]
        else:
            d[s_sorted].append(s)
    return list(d.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if not s_sorted in d.keys():
                d[s_sorted] = [s]
            else:
                d[s_sorted].append(s)
        return list(d.values())
        



        
# @lc code=end


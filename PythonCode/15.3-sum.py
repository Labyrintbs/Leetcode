#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# @lc code=start

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums_sorted = list(nums)
        n = len(nums_sorted)
        res = [] 
        if n <3:
            return res 
        nums_sorted.sort()
        for i in range(n-1):
            if nums_sorted[i] > 0:
                break
            if i >0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            l ,r = i+1, n-1 
            while l<r:
                res_temps =nums_sorted[l] + nums_sorted[i] + nums_sorted[r]  
                list_temps = [nums_sorted[l],nums_sorted[i],nums_sorted[r]]
                if res_temps > 0 :
                    r -=1
                elif res_temps <0: 
                    l += 1
                else:
                    if list_temps not in res:
                        res.append(list_temps) 
                    l+=1
        return res
'''
            l ,r = i-1, i+1
            while r <= n-1 and l >=0:
                res_temps =nums_sorted[l] + nums_sorted[i] + nums_sorted[r]  
                list_temps = [nums_sorted[l],nums_sorted[i],nums_sorted[r]]
                if res_temps == 0 and list_temps not in res:
                   res.append(list_temps) 
                elif res_temps > 0 :
                    l -=1
                else:
                    r +=i1
            l ,r = 0, n-1 
            while l<i<r:
                res_temps =nums_sorted[l] + nums_sorted[i] + nums_sorted[r]  
                list_temps = [nums_sorted[l],nums_sorted[i],nums_sorted[r]]
                if res_temps == 0 and list_temps not in res:
                   res.append(list_temps) 
                elif res_temps > 0 :
                    r -=1
                else:
                    l +=1
            l ,r = i+1, n-1 
            while nums_sorted[i]<0:
                while l < r :
                    res_temps =nums_sorted[l] + nums_sorted[i] + nums_sorted[r]  
                    list_temps = [nums_sorted[l],nums_sorted[i],nums_sorted[r]]
                    if res_temps == 0 and list_temps not in res:
                        res.append(list_temps) 
                    elif res_temps > 0 :
                        r -=1
                    else:
                        l +=1
            return res
        

def threeSum(nums):
        nums_sorted = list(nums)
        n = len(nums_sorted)
        res = [] 
        if n <3:
            return res 
        nums_sorted.sort()
        for i in range(n-1):
            if nums[i] > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            l ,r = i+1, n-1 
            while i<l<r:
                res_temps =nums_sorted[l] + nums_sorted[i] + nums_sorted[r]  
                list_temps = [nums_sorted[l],nums_sorted[i],nums_sorted[r]]
                if res_temps == 0 and list_temps not in res:
                   res.append(list_temps) 
                elif res_temps > 0 :
                    r -=1
                else:
                    l +=1
        return res

print(threeSum([1,0,-1]))
'''
# @lc code=end


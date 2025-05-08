"""
217 Contains Duplicates, Easy
Given Integer array, nums, return true if any value appears more than once in array, otherwise return False.

nums = [1,2,3,4,5] , False
nums = [2,3,4,4] , True
"""

class Solution:
    def bruteForce(self, nums : [int]) -> bool :
        # Loop through nums
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                """WRONG:
                if i == j:
                """
                if nums[i] == nums[j]:
                    return True
        return False
    
    def sorting(self, nums : [int]) -> bool :
        #sort nums
        nums.sort()
        # loop through sorted nums
        """WRONG:
         for i in range(len(nums)):
         
         On the first iteration, i = 0, so nums[i - 1] = nums[-1] → wraps to the last item in the list by accident.
         false positive or error when comparing the first element with the last one
        """
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def hashmap(self, nums : [int]) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                return True
            hm[nums[i]] = 1 + hm.get(nums[i], 0)
        return False
    
    """Easier way: Hashset"""
    def hashset(self, nums : [int]) -> bool:
        """WRONG:
        hs = []
        """
        hs = set()
        for i in range(len(nums)):
            if nums[i] in hs:
                return True
            hs.add(nums[i])
        return False
        
sol = Solution()
result1 = sol.hashset([1,2,3,4,5]) #False
result2 = sol.hashset([1,2,3,3,4]) #True
result3 = sol.hashset([42]) #False
print(result1, result2, result3)
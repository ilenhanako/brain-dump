'''
Given array of int nums and an int target, 
return indices i and j such that nums[i] + nums[j] == target
i != j

Inputs: nums: [2,7,11,15], target = 9
Output: [1,2]

Inputs: nums:[3,3], target = 6
Output: [0,1]
'''

class Solution:
    def twoSum(self, nums : [int], target : int) -> [int] : #output is array of index
        # 1: create hashmap
        hashmap = {}
        # 2: loop through the array, since we want both the index and the value use enumerate()
        for index,num in enumerate(nums):
        # 3: diff = target - num
            diff = target - num
        # 4: Check for existence of diff in hashmap, if diff exists in hashmap
            if diff in hashmap:
        # 5: return the array of index of num and the diff(value in hashmap)
                return [index , hashmap.get(diff)]
        # 6: else add the num into the hashmap
            hashmap[num] = index
            
sol = Solution()
result1 = sol.twoSum([11,2,7,15], 9) #[2,1]
result2 = sol.twoSum([3,3], 6) #[0,1]
print(result1, result2)
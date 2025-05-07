from typing import List

class Solution:
    def twoSum(self, nums : List[int] , target : int) -> List[int] :
        # index == values, num == keys        
        hashmap = {}
        
        # loop through nums to get the index and num
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], index]
            # add the num into the hashmap if it's not the diff
            hashmap[num] = index
        return

sol = Solution()
result1 = sol.twoSum([2, 7, 11, 15], 9)
result2 = sol.twoSum([3,4,5,6], 7)
result3 = sol.twoSum([2,5], 7)
print(result1, result2, result3)  # Output: [0, 1], [0,1], [0,1]
        
        
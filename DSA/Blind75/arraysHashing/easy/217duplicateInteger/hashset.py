# 217 Contains Duplicates, Easy
# Given Integer array, nums, return true if any value appears more than once in array, otherwise return False.
# nums = [1,2,3,4,5] , False
# nums = [2,3,4,4] , True

"""SOL 3: Hash Set (Optimal)
use hashSet, if num doesn't exist in hashSet then add, if exist then return True
initialise hashSet
O(n) time, takes O(1) to check for integer by the hash function and O(n) as the loop iterates over each element in the array
O(n) space
"""

def duplicateInt(nums):
    hashSet = set()
    #iterate through array to find duplicate
    for num in nums:
        #check for existence of integer in hashset
        if num in hashSet:
            return True
        #if not exist then add to hashSet
        hashSet.add(num)
        return False
    
nums = [1,2,3,4,5]
print(duplicateInt(nums))
        
# 217 Contains Duplicates, Easy
# Given Integer array, nums, return true if any value appears more than once in array, otherwise return False.
# nums = [1,2,3,4,5] , False
# nums = [2,3,4,4] , True
"""SOL 1: Brute Force
Compare the number with every number on its right.
Repeat with the next number.

O(n^2) time
O(1) space

# WRONG
def duplicateInt(nums):
    for n in range(len(nums)):
        if nums[n] == nums[n+1]:
            return True
    return False
""" 

def duplicateInt(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
    
nums = [1,2,3,4,5]
print(duplicateInt(nums))
        
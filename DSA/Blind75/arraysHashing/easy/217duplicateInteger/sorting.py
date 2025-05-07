# 217 Contains Duplicates, Easy
# Given Integer array, nums, return true if any value appears more than once in array, otherwise return False.
# nums = [1,2,3,4,5] , False
# nums = [2,3,4,4] , True
"""SOL 2: Sorting
Sort the array.
Compare the number with the number that is adjacent to it. Repeat with the next number.
O(nlogn) time
O(1) space

# WRONG: Out of range
def duplicateInt(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            return True
    return False
""" 

def duplicateInt(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
    
        
    
nums = [1,2,3,4,5]
print(duplicateInt(nums))
        
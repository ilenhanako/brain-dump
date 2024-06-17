# 1 Two Sum, Easy

'''
Given array of int nums and an int target, 
return indices i and j such that nums[i] + nums[j] == target
i != j

Inputs: nums: [2,7,11,15], target = 9
Output: [1,2]

Inputs: nums:[3,3], target = 6
Output: [0,1]
'''

def twoSum(nums, target):
    #key = value of each integer
    #value = index of each integer
    hashMap = {}
    #i = index of current element
    #n = value of current element
    for i,n in enumerate(nums):
        #calc for difference between target and value of current
        diff = target - n
        #check if difference exists in hashmap
        if diff in hashMap:
            #if yes, means we have already encountered a number in the list that can be added to n to reach target
            #return index i and j
            return [hashMap[diff], i]
    return
    
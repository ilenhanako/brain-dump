#june11, 204 Binary Search, Easy

#You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
#Your solution must run in 𝑂(𝑙𝑜𝑔𝑛) time.

def binarySearch(nums):
    # initialise pointers
    left = 0
    right = len(nums) - 1
    # loop through nums to ensure left < right
    while left <= right:
        mid = (left + right) // 2 #calc middle
        if nums[mid] > target: #middle value is greater than target
            right = mid - 1 #move right pointer to check for the numbers before middle value
        elif nums[mid] < target: #middle value is smaller than target
            left = mid + 1 #move left pointer to check for numbers after middle value
        else:
            return mid
    return -1

nums = [2,6,7,8,9,10,12]
target = 7
result = binarySearch(nums)
print(result)
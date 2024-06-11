
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
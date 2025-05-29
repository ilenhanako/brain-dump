'''
128. Longest Consecutive Sequence (Medium)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    def longest_consecutive_elements(self, nums):
        longest = 0
        # for each number in array
        for num in nums:
            current = num
            count = 1
            
            #keep checking if next num exists (check if able to build consec sequence)
            while current + 1 in nums:
                current += 1
                count += 1 # how long current conseq is 
            # find out the max 
            longest =  max(longest, count)
        return longest
    
    def sort_elements(self, nums):
        # Initial nums = [100, 4, 200, 1, 1, 3, 2]
        # edge case: empty list, return 0
        if not nums:
            return 0
        
        #sort the array  --> O(nlogn)
        nums.sort() #[1,1,2,3,4,100,200]
        
        # initialize variables
        # keep track of longest sequence found
        longest = 1
        # count current sequence length
        count = 1    
        
        # Iterate through the sorted list
        for i in range(1, len(nums)):
            # [1,1,2] skip duplicates
            if nums[i] == nums [i-1]:
                continue
            
            #check if current number is exactly 1 greater than previous
            elif nums[i] == nums[i-1] + 1:
                count +=1 #continues the current sequence
                longest = max(longest, count) # check if current count is larger, if it is then it will update
        return longest 
            
        
sol = Solution()
result1 = sol.longest_consecutive_elements([100, 4, 200, 1, 1, 3, 2]) #[1,1,2,3,4,100,200] , 4
result2 = sol.sort_elements([100, 4, 200, 1, 1, 3, 2]) # 4

#empty list
result3 = sol.sort_elements([]) # 0
#single element
result4 = sol.sort_elements([42]) #1
#all duplicates
result5 = sol.sort_elements([2,2,2]) # 1
#already conseq
result6 = sol.sort_elements([1,2,3,4,5]) # 5
#negative numbers
result7 = sol.sort_elements([-2, -1,0,6,1])#4
print(result1,result2,result3,result4,result5,result6,result7)
                
'''
3. Longest Substring w/o Repeats

Given a string s, find the length of the longest substring without duplicate characters.

random
In: "abcabcbb"

index j[3]: a

index i[0]: a

how to get length abc?
j-i= 2

all the same
In: "bbbbbbb"

In: "3"
'''
class Solution:
#brute force
    def brute_force(self, str):
        #initialize variables 
        max_length = 0
        #how to store unique chracters?set
        seen = set()

        #check every possible substring (loop)
        for i in range(len(str)):
            for j in range(1, len(str)):
                if str[j] in seen:
                    break # duplicates found --> break the inner loop
                seen.add(str[j]) #add current character to set
                max_length = max(max_length, j-i)                
        return max_length
    
sol = Solution()
result = sol.brute_force("abcabcbb") #3
result1 = sol.brute_force("bbbbb") #1
result2 = sol.brute_force("iaosjdf") #6
result3 = sol.brute_force("iwwki") #3 #eerrroorororororor
print(result, result1,result2,result3)
        
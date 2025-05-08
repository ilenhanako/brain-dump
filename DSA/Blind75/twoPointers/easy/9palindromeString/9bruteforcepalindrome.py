"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Input: s = "Was it a car or a cat I saw?"
Output: true
"""

### BRUTE FORCE
# Loop through string, create a new alphanumerical string, check for alphanumerical character, 
# make lowercase, reverse string and check if equal

class Solution:
    def isPalindrome (self, s:str) -> bool:
        newS = "" #make a alphanumerical str
        for c in s:
            if c.isalnum():
                newS += c.lower()
        return newS == newS[::-1]
    
sol = Solution()
result1 = sol.isPalindrome("Was it a car or a cat I saw?") #True
result2 = sol.isPalindrome("lalalala") #False
print(result1, result2)
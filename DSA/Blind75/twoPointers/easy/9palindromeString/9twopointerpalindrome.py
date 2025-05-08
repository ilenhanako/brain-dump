"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Input: s = "Was it a car or a cat I saw?"
Output: true

Input: s = "No lemon, no melon"
Output: True
"""

### Two Pointer & w/o built-in alphanumeric function

class Solution:
    def alphanumeric(self, c:str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    def twoPointer(self, s:str) -> bool:
        left ,right = 0, len(s) - 1
        
        while left <= right:
            if not self.alphanumeric(s[left]):
                left += 1
                "REMEMBER TO ADD: continue STILL DONT UNDERSTAND WHY...."
                continue
                
            if not self.alphanumeric(s[right]):
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
    
sol = Solution()
result1 = sol.twoPointer("Was it a car or a cat I saw?") #true
result2 = sol.twoPointer("No lemon, no melon") #true
print(result1, result2)
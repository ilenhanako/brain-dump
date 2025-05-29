"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise."""

class Solution:
    def validParenthesis(self, s:str) -> bool:
        stack = []
        hashmap = {"]":"[", ")" : "(", "}" : "{"}
        
        for c in stack:
            #check if c is a closing bracket
            if c in hashmap.keys():
                
                #check if stack is not empty and last element is corresponding opening bracket
                if stack != [] and stack[-1] == hashmap.values(c):
                    # pop out opening bracket of stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        #return True if stack is empty, else False
        return True if stack == [] else False
        
sol = Solution()
result1 = sol.validParenthesis("{([])}") #true
result2 = sol.validParenthesis("{{([]}}") #false
result3 = sol.validParenthesis("[]") #true
print(result1, result2, result3)

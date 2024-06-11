# June 10, 20 Valid Parenthesis, Easy
# Idea: Stack, Hashmap

def validParenthesis(s):
    #initialise stack
    stack = []
    hashMap = {")": "(", "}" : "{", "]" : "["} # Hashmap to link all the different brackets
    for bracket in s: # loop through s
        if bracket in hashMap: #check if its a closed bracket
            #check if stack is empty(we need presence of opening bracket)
            #check if top of stack is the matching opening bracket
            if stack and stack[-1] == hashMap[bracket]: 
                #if yes, remove the opening bracket from the stack
                stack.pop()
            else:
                #if stack empty of no match
                return False
        else: #not a closed bracket
            stack.append(bracket)
    #if at the end, the stack is empty, all matches found
    if stack == []:
        return True
    else:
        return False
                
s = " " #Output: True
print(validParenthesis(s))
#s = "({])" #Output: False

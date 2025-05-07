# 9 Palindrome Number

'''
Given integer x, return true if x is a palindrome and false otherwise.

Input: x = 121
Output: true

Input: x = 54321
Output: false
'''

'!!!!! PALINDROME = 2 POINTER QUESTION !!!!!!'

def palindromeNumber(x):
    x = str(x)
    start = 0
    end = len(x)-1
    
    #Loop till pointers in middle, start cannot cross end
    while start <= end:
        if x[start] == x [end]:
            start += 1
            end -= 1
            return True
    return False
        
x = 121
print(palindromeNumber(x))
'''
Documented Errors:
ATTEMPT 1: error as integer has no len()
SOLUTION 1: convert int to str. str()
'''

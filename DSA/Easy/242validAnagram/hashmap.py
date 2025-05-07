# 242 validAnagram, Easy
"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"
Output: true
"""

# SOL1: HashMap {}
"Alphabets == Keys, Frequency == Values. Check if the values of the 2 hashmaps are the same for the corresponding keys"

def isAnagram(s,t):
    # check if the length of strings are the same. If not return False
    if len(s) != len(t):
        return False
    
    # set up hashmap
    countS, countT = {} , {}
    for i in range(len(s)): # Loop through string S
        countS[s[i]] = 1 + countS.get(s[i], 0)
    for j in range(len(t)):
        countT[t[j]] = 1 + countT.get(t[j], 0)
        
    # compare hashmap
    for k in countS.keys(): # Loop through the keys of one of the hashmaps
        """ WRONG: Code is saying If any one character count matches, return True 
        if countS[k] == countT.get(k, 0):
            return True
    return False
    """
        if countS[k] != countT.get(k, 0):
            return False
    return True 

s, t = "racecar", "carrace"
print(isAnagram(s,t))
    
    
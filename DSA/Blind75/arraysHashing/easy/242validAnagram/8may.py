# 242 validAnagram, Easy
"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"
Output: true
"""

class Solution:
    def isAnagram(s:str, t:str) -> bool:
        
        "FORGOT TO CHECK FOR LENGTH!!"
        if len(s) != len(t):
            return False
        
        countS , countT = {}, {}
        for char in range(len(s)):
            
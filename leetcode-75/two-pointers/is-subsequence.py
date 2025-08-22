"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

racters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the cha"abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution(object):
    def isSubsequence(self, s, t):

        if not s:
            return True

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        if i == len(s) :
            return True
        else:
            return False                
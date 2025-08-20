"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
"""

class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        vowelsYakalayici = []

        for ch in s:
            if ch in vowels:
                vowelsYakalayici.append(ch)
        vowelsYakalayici.reverse()

        result = []
        for ch in s:
            if ch in vowels:
                result.append(vowelsYakalayici.pop(0))
            else:
                result.append(ch)

        return "".join(result)            
            

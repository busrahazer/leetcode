"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
 such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
"""

# My solution (I think it's true but not enough for leetcode)
class Solution(object):
    def increasingTriplet(self, nums):
        for i in range(len(nums)):
            if nums[i-1] < nums[i] < nums[i+1] in nums:
                return True               
        return False       
         
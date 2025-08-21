"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

# O(n*2) solutionclass Solution(object):
def productExceptSelf(self, nums):

        without_n = []
        result = 1
        final_result = []

        for i in range(len(nums)):
            without_n = nums[:i] + nums[i+ 1:]
            result = 1

            for j in without_n:
                result *= j
            final_result.append(result)
                
        return final_result    
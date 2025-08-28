"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""

# My Solution but for litte arrays it works
class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        nums_copy = nums[:]

        while nums_copy:
            found = False

            for i in range(len(nums_copy)):
                for j in range(i+1, len(nums_copy)):
                    if nums_copy[i] + nums_copy[j] == k:
                        nums_copy.pop(j)
                        nums_copy.pop(i)
                        count +=1
                        found = True
                        break
                if found:
                    break
            if not found:
                break

        return count    

# Optimal Solution
class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        freq = {} 

        for num in nums:
            complement = k - num
            if freq.get(complement, 0) > 0:
                count += 1
                freq[complement] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
        return count
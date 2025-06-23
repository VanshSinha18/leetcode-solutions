# Problem 1: Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map to store index-value pairs
        h = {}

        # loop through the loop with index and value
        for i, num in enumerate(nums):
            # complement needed to reach the target
            y = target - num
            # if the complement exists in the hashmap
            if y in h:
                # return the indices as a list
                return [h[y], i]
            # otherwise store the current num and its index
            h[num] = i

# test cases
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Expected: [0, 1]
print(sol.twoSum([3,2,4], 6))      # Expected: [1, 2]
print(sol.twoSum([3,3], 6))        # Expected: [0, 1]

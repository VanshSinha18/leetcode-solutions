# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# idea here is that we first find the expected sum of the numbers from 0 to n
# then we find the actual sum of the numbers in the array
# the difference between the expected sum and the actual sum is the missing number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

print(Solution().missingNumber([3,0,1]))

# explanation:
# 1. we find the expected sum of the numbers from 0 to n
# 2. we find the actual sum of the numbers in the array
# 3. we return the difference between the expected sum and the actual sum
# 4. this is the missing number
# 5. we use the formula for the sum of an arithmetic series to find the expected sum
# 6. we use the sum function to find the actual sum
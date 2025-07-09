# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# idea here is that we use a set to store the numbers in the array
# then we iterate through the range [1, n] and check if the number is in the set
# if it is not, we add it to the result list

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        ret = []

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                ret.append(i)
        
        return ret
    
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))

# explanation:
# 1. we convert the list to a set to remove duplicates
# 2. we iterate through the range [1, n] and check if the number is in the set
# 3. if it is not, we add it to the result list
# 4. we return the result list
    
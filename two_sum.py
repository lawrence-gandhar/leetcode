"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

import time

class Solution:
    def twoSum(self, nums, target: int):
        li = list(enumerate(nums))
        li.sort(key=lambda x: x[1])

        for i in range(len(li)):
            for j in range(i+1, len(li)):
                if li[i][1] + li[j][1] == target:
                    return [li[i][0], li[j][0]]

    def twoSum2(self, nums, target: int):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSum3(self, nums, target: int):

        x = [(i,j) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] + nums[j] == target]
        return list(x[0])

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

nums = [-3,4,90,-1,-2,100,40,34,12,3]
target = 0

s = Solution()
start_time = time.time()
print(s.twoSum(nums, target))
end_time = time.time()
print("Time : ", end_time-start_time)

start_time = time.time()
print(s.twoSum2(nums, target))
end_time = time.time()
print("Time : ", end_time-start_time)

start_time = time.time()
print(s.twoSum3(nums, target))
end_time = time.time()
print("Time : ", end_time-start_time)
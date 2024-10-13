"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):

        xx = len(nums)
        for i in range(xx - 1):
            for j in range(i+1, xx):
                if nums[i] == nums[j]:
                    if abs(i-j) <= k:
                        # print("found", nums, i, j, nums[i], nums[j], abs(i - j), k)
                        return True
        else:
            # print("not found", nums, i, j, nums[i], nums[j], abs(i - j), k)
            return False

    def method2(self, nums, k):
        dict1 = {}

        for i in range(len(nums)):
            if nums[i]  in dict1 and abs(i - dict1[nums[i]]) <= k:
                return True
            dict1[nums[i]] = i 
        return False



t1, k1 = [1,2,3,1], 3
t2, k2 = [1,0,1,1], 1
t3, k3 = [1,2,3,1,2,3], 2
t4 = [2,14,18,22,22]

ss = Solution()
ss.containsNearbyDuplicate(t1, k1)
ss.containsNearbyDuplicate(t2, k2)
ss.containsNearbyDuplicate(t3, k3)
# ss.containsNearbyDuplicate(t4)
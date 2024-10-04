"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class Solution:
    def singleNumber(self, nums):

        xx = len(nums)
        i = 0
        while i < xx:
            
            if xx == 1:
                return nums[0]

            for j in range(i+1, xx):
                # print(i, j, nums)
                if nums[i] == nums[j]:
                    del nums[j]
                    del nums[i]
                    i = 0
                    xx = len(nums)
                    # print(i, j, nums)
                    break
                else:
                    if j == xx - 1:
                        return nums[i]
            else:
                i += 1
                
        return nums[0]

    #
    # Above method takes O(n^2)
    #

    
    def method2(self, nums):
        start = 0
        end = 1
        
        if len(nums) == 1:
            return nums[0]

        while True:
            if end > len(nums) - 1 :
                break

            if end == len(nums) - 1:
                start += 1
                end = start + 1

            if nums[start] == nums[end]:
                del nums[end]
                del nums[start]
                start = 0
                end = 1
            else:
                end += 1
            print(nums, start, end)
        return nums[start]

# t1 = [2,2,1]
# t2 = [4,1,2,1,2]
t3 = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]

ss = Solution()

# ss.singleNumber(t1)
# ss.singleNumber(t2)
print(ss.singleNumber(t3))

# print(ss.method2(t1))
# print(ss.method2(t2))
# print(ss.method2(t3))
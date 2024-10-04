"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        xx = len(nums)

        if xx > 1:
            i = 0
            j = 0 
            while i < xx:
                print(i, xx, nums)
                if nums[i] == 0:
                    del nums[i]
                    nums = nums + [0]
                    j -= 1
                    xx = len(nums[i:j])
                else:
                    i += 1

    def method2(self, nums):
        
        xx = len(nums)
        start = 0
        i = 1
        while i < xx - 1:

            # print("before process", nums, start, xx, i)

            if nums[i] == 0:
                del nums[i]
                nums = nums + [0]
                xx -= 1 
        
            if nums[start] == 0:
                del nums[start]
                nums = nums + [0]
                xx -= 1 

            if nums[i] != 0 and nums[start] != 0:
                i += 1

            # print("after process", nums, start, xx, i)
            

    def method3(self, nums):   
        start = 0
        next_i = 1

        if len(nums) > 1:
            while next_i < len(nums):
                if nums[start] == 0 and nums[next_i] == 0:
                    next_i += 1
                else:
                    if nums[start] == 0:
                        nums[start], nums[next_i] = nums[next_i], nums[start]
                    start += 1
                    next_i += 1
                
                print(nums)

t1 = [0,1,0,3,12]
t2 = [0]
t3 = [1,0]

ss = Solution()
# ss.moveZeroes(t1)
# ss.moveZeroes(t2)

# ss.method2(t1)

ss.method3(t3)
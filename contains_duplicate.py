"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def containsDuplicate(self, nums):
        xx = len(nums)
        for i in range(xx):
            for j in range(i+1, xx):
                if nums[i] == nums[j]:
                    return True
        return False
    

    def method2(self, nums):
        j = 1
        i = 0
        xx = len(nums)
        while i < xx:
            while j < xx:
                if nums[i] == nums[j]:
                    return True
                else:
                    j += 1
            
            j = i + 1
            i +=1 
            
        return False
    

    def method3(self, nums):
        xx = iter(nums)
        xx1 = iter(nums[1:])
        c = 1
        for i in xx:
            for j in xx1:
                print("inc", i, j)
                if i == j:
                    return True
            c += 1 
            xx1 = iter(nums[c:])
        return False
    

    def method4(self, nums):
        return len(nums) == len(set(nums))



t1 = [1,2,3,1]
t2 = [1,2,3,4]
t3 = [1,1,1,3,3,4,3,2,4,2]
t4 = [2,14,18,22,22]

ss = Solution()
# ss.containsDuplicate(t1)
# ss.containsDuplicate(t2)
# ss.containsDuplicate(t3)

print(ss.method3(t4))

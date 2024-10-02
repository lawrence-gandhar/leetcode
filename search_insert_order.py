"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. \
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums, target):
        
        start = 0
        end = len(nums) - 1

        while start <= end:

            print(start, end)

            mid = (start + end)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return end + 1


       

        


t0, tar0 = [1,3,5,6], 0
t1, tar1 = [1,3,5,6], 5
t2, tar2 = [1,1,1,1,3,5,6], 2
t3, tar3 = [1,3,5,6], 7
t4, tar4 = [1,3,5,6,7,9,11], 7
t5, tar5 = [1,3,5,6,8,9,11], 4
t6, tar6 = [1,1,1,3,5,6,8,9,11,12,15,18,22,24,28,29,31,45,56,89,90,91], 10

ss = Solution()

print("=" * 20)
print(ss.searchInsert(t0, tar0))      
print("=" * 20) 
print(ss.searchInsert(t1, tar1))   
print("=" * 20)
print(ss.searchInsert(t2, tar2))  
print("=" * 20)
print(ss.searchInsert(t3, tar3)) 
print("=" * 20)
print(ss.searchInsert(t4, tar4)) 
print("=" * 20)
print(ss.searchInsert(t5, tar5)) 
print("=" * 20)
print(ss.searchInsert(t6, tar6)) 
print("=" * 20)
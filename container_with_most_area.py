"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:
    def maxArea(self, height):

        max_area = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if height[i] <= height[j]:
                    area = (j-i) * height[i]
                elif height[i] > height[j]:
                    area = (j-i) * height[j]

                if area > max_area:
                    max_area = area 

                # print("j-i", j-i,"max_area", max_area, "area", area, "i", i, "j", j, "height i val", height[i], "height j val", height[j])
                # print("===========")
        
        return max_area

    # shifting pointers method
    # faster then brute force
    def method2(self, height):
        start_index = 0
        end_index = len(height) - 1
        max_area = 0
        area = 0

        while start_index < end_index:

            if height[start_index] <= height[end_index]:
                area = height[start_index] * (end_index - start_index)
                start_index += 1
            elif height[start_index] > height[end_index]:
                area = height[end_index] * (end_index - start_index)
                end_index -= 1 
            
            max_area = area if area >= max_area else max_area

            # print(start_index, end_index, area)
        print(max_area)
        return max_area


t1 = [1,8,6,2,5,4,8,3,7]
t2 = [1,1]
t3 = [1,2,4,1,5,7]
ss = Solution()
# print(ss.maxArea(t1))
# print(ss.maxArea(t2))
# print(ss.maxArea(t3))

ss.method2(t1)
ss.method2(t2)
ss.method2(t3)

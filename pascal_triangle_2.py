"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

class Solution:
    def getRow(self, rowIndex):

        numRows = rowIndex + 1
        
        if numRows == 1:
            return [1]
        
        ff = []
        for x in range(numRows):
            xx = [1 for k in range(x+1)]
            ff.append(xx)

            if x+1 >= 3:
                l = 0
                while l < len(ff[x-1]) - 1:
                    ff[x][l+1] = ff[x-1][l] + ff[x-1][l+1]
                    l += 1
        # print(ff[rowIndex])
        return ff[rowIndex]
    

test = 8
ss = Solution()
ss.generate(test)
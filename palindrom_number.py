"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        temp = x
        if x < 0:
            return False
   
        while temp > 0:
            result = (result*10) + (temp%10)
            temp = temp//10
        if result == x:
            return True
        return False
    
import time
x = 321123
ss = Solution()

start = time.time()
print(ss.isPalindrome(x))
print(time.time() - start)

start = time.time()
print(ss.isPalindrome2(x))
print(time.time() - start)
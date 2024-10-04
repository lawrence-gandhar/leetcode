"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""




t1 = "Hello World"
t2 = "   fly me   to   the moon  "
t3 = "luffy is still joyboy"
t4 = ""

class Solution:
    def plusOne(self, digits):
        len_l = len(digits)
        x = iter(digits)
        sum = 0

        i = 0
        j = len_l - 1
        while i < len_l:
            sum += next(x) * (10 ** j)
            i += 1
            j -= 1 

        return [int(f) for f in str(sum+1)]
    

    def method2(self, digits):
        if digits[0] == 9:
            digits = [0] + digits

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else: 
            i = len(digits) - 1
            remaindar = 0 
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    remaindar = 1

                    if i == 0 and remaindar == 1:
                        digits = [1] + digits
                        return digits
                else:
                    if digits[i] < 9:
                        digits[i] = digits[i] + remaindar
                        break
                i -= 1

            return digits


t1 = [9,8,7,6,5,4,3,2,1,0]
t2 = [4,3,9,9]
t3 = [9]

ss = Solution()

print("="*20)
print(ss.plusOne(t1))
print("="*20)
print(ss.plusOne(t2))
print("="*20)
print(ss.plusOne(t3))

print("="*20)
print(ss.method2(t1))
print("="*20)
print(ss.method2(t2))
print("="*20)
print(ss.method2(t3))
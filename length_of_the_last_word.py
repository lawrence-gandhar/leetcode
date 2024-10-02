"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])

    #   without using built-in functions
    # ============================================
    def method2(self, s):
        found_char = False

        i = len(s) - 1
        count = 0 

        for i in range(i, -1, -1):
            if not found_char:
                if s[i] != " ":
                    count += 1
                    found_char = True
            else:
                if s[i] == " ":
                    break   
                else:
                    count += 1                     

        return count


t1 = "Hello World"
t2 = "   fly me   to   the moon  "
t3 = "luffy is still joyboy"
t4 = ""

ss = Solution()

print("="*20)
print(ss.lengthOfLastWord(t1))
print("="*20)
print(ss.lengthOfLastWord(t2))
print("="*20)
print(ss.lengthOfLastWord(t3))
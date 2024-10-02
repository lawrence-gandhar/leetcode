"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        
        ss = re.search(needle, haystack)

        if ss is not None:
            return ss.span()[0]
        else:
            return -1



import time
x = "sndbutsad"
y = "sad"
ss = Solution()

start = time.time()
print(ss.strStr(x,y))
print("Time :: ", time.time() - start)
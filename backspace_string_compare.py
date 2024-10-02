"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s, t: str) -> bool:
        import gc
        s1 = list(s)
        t1 = list(t)

        del s
        del t

        gc.collect()

        s1.append("%")
        s1.extend(t1)
        i=0
        while i < len(s1):
            print(i, s1)
            if s1[i] == "#":
                if i == 0 and s1[i] == "#":
                    del s1[0]
                    i = 0
                if i+1 < len(s1):
                    if s1[i-1] != "%":
                        del s1[i-1:i+1]
                        i = 0
                    else:
                        del s1[i]
                        i = 0
                else:
                    if s1[i-1] != "%":
                        del s1[i-1:i+1]
                        i = 0
                    else:
                        del s1[i]
                        break
            else:
                i += 1
        print(s1)
        d, c = "".join(s1).split("%")
        return d==c


import time
x = "hd#dp#czsp#####"
y = "hd#dp#czsp#######"
ss = Solution()

start = time.time()
print(ss.backspaceCompare(x,y))
print("Time :: ", time.time() - start)
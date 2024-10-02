"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s):
        self.t = {
            "(":')', 
            '{':'}', 
            '[':']'
        }

        self.open_b = self.t.keys()
        self.closed_b = self.t.values()

        self.s = s

        found = False
        len_s = len(self.s)
        i = 0

        if len_s % 2 != 0:
            # print(False)
            return False 

        while i < len_s:
            # print("Value of i ",i , len_s, self.s[i])
            if self.s[i] in self.t:
                if self.s[i+1] in self.closed_b and self.s[i+1] != self.t[self.s[i]]:
                    # print("process stopped at ", i, self.s, False)
                    return False
                else:
                    if self.s[i+1] in self.open_b:
                        # print(self.s, "found open b")
                        cc = self.find_open_p(i)
                        if cc:
                            i = 0
                            len_s = len(self.s)
                            # print("value reset ", i, len_s)
                            return self.isValid(self.s)
                        else:
                            # print("stopped the process", cc)
                            return cc
                    else:
                        if self.s[i+1] == self.t[self.s[i]]:
                            if len_s == 2:
                                found = True
                                i += 1
                                # print("else block stopped", i, self.s, found)
                                return found
                            else:
                                cc = self.find_open_p(i)
                                if cc:
                                    i = 0
                                    len_s = len(self.s)
                                    # print("value reset ", i, len_s)
                                    return self.isValid(self.s)
                                else:
                                    # print("stopped the process", cc)
                                    return cc
            else:
                # print("else block stopped 2",self.s, False)
                return found  
            
            i += 1   

    def find_open_p(self, i):
        if self.s[i] in self.open_b:
            # print("found open traversing", self.s[i], i)
            i += 1
            # print(" next i before calling open_p", i)
            return self.find_open_p(i) 
        else:
            # print("found closed stopping", self.s[i], i)
            if self.find_close_p(i):
                # print(self.s[i-1:i+1])
                self.s = self.s.replace(self.s[i-1: i+1], "")
                # print("new string formed", self.s)
                return True

    def find_close_p(self, i):
        if self.s[i] in self.closed_b:
            if self.t[self.s[i-1]] == self.s[i]:
                # print("closest parent found", self.s[i-1], i)
                return True 
            else:
                # print("not a valid parent", self.s[i-1], self.s[i], i)
                return False
        # print("No parent")
        return False



t1 = "()"
t2 = "()[]{}"
t3 = "()[]{}]"
t4 = "(]"
t5 = "([])"
t6 = "({[()]})]["
t7 = "({[[({})]]})"

ss = Solution()
# print("="*10)
# print("t1", t1)
# print("="*10)
# ss.isValid(t1)
# print("="*10)
# print("t2", t2)
# print("="*10)
# ss.isValid(t2)
# print("="*10)
# print("t3", t3)
# print("="*10)
# ss.isValid(t3)
# print("="*10)
# print("t4", t4)
# print("="*10)
# ss.isValid(t4)
# print("="*10)
# print("t5", t5)
# print("="*10)
# ss.isValid(t5)
# print("="*10)
# print("t6", t6)
# print("="*10)
# ss.isValid(t6)
# print("="*10)
# print("t7", t7)
# print("="*10)
# ss.isValid(t7)
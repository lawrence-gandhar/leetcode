"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, list1):
        self.list1 = list1
        self.list1.sort(key = lambda x: len(x))

        print(len(self.list1))

        if len(self.list1) >= 2:
            # self.create_combinations()
            self.method2()
        else:
            print(self.list1[0])

    # Create Combinations for the smallest string
    # Iterate through the the remaining list
    # ==============================================================
    def create_combinations(self):     
        xx = len(self.list1[0])
        wq = len(self.list1[1:])

        found_list = {}

        combinations = [self.list1[0][:x] for x in range(xx, 0, -1)]

        count = 0
        
        combination_len = len(combinations)
        combinations = iter(combinations)

        while count < combination_len:
            cc = next(combinations)
            found = 0
            
            main_list_iter = iter(self.list1[1:])

            while True:
                
                try:
                    mm = next(main_list_iter)

                    print(mm.startswith(cc))

                    if mm.startswith(cc):
                        found = found+1
                        found_list.update({cc: found})
                    else: 
                        found -= 1

                    # print(cc, mm, found)
                except:
                    break
            count +=1    

        jj = found_list.copy()

        for key, value in jj.items():
            if value < wq:
                del found_list[key]

        del jj

        print(found_list)

        if len(found_list) > 0:
            temp = list(found_list)[0]
            for key in found_list.keys():
                if len(key) > len(temp):
                    temp = key

            print(temp)
        else:
            print("found ==> ","")


    def method2(self):
        xx = len(self.list1[0])
        wq = len(self.list1[1:])

        found_list = {}

        combinations = [self.list1[0][:x] for x in range(xx, 0, -1)]

        print("combinations", combinations)

        for xx in self.list1[1:]:
            for jj in combinations:

                print(xx, jj, xx.startswith(jj))

                if xx.startswith(jj):
                    found_list.update({jj: found_list[jj]+1 if jj in found_list else 1})
                else: 
                    found_list.update({jj: found_list[jj]-1 if jj in found_list else -1})

        jj = found_list.copy()

        print(jj)

        for key, value in jj.items():
            if value < wq:
                del found_list[key]

        print(found_list)

        if len(found_list) > 0:
            temp = list(found_list)[0]
            for key in found_list.keys():
                if len(key) > len(temp):
                    temp = key

            print("found ==> ",temp)
        else:
            print("found ==> ","")





list1 = ["flower","fansss","flight"]
list2 = ["dog","racecar","car"]
list3 = ["flower","flow","flight"]
list4 = ["a"]
list5 = ["ab", "a"]
list6 = ["cir","car"]
list7 = ["reflower","flow","flight"]
list8 = ["aa","aa"]
list9 = ["aca","cba"]

ss = Solution()
df = ss.longestCommonPrefix(list1)
df = ss.longestCommonPrefix(list2)
df = ss.longestCommonPrefix(list3)
df = ss.longestCommonPrefix(list4)
df = ss.longestCommonPrefix(list5)
df = ss.longestCommonPrefix(list6)
df = ss.longestCommonPrefix(list7)
df = ss.longestCommonPrefix(list8)
df = ss.longestCommonPrefix(list9)


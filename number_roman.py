"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999
"""

class Solution:

    """
        arr = [1, 5, 10, 50, 100, 500, 1000]
        mid = 7//2 => 3
        low = arr[0] => 1, mid = arr[mid] =>50, high = arr[-1] => 1000

        if x < arr[mid]:
            then 
                high = arr[mid] => arr[4] => 50
                low = arr[0] => 1   
                mid = len(arr[low:high])//2 => 2
    """

    def intToRoman(self, num: int) -> str:
        dict1 = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        result = []
        
        num_list = list(str(num))
        dict_keys = list(dict1.keys())
        len_dict_keys = len(dict_keys)
        num_list.reverse()
        num_list = list(map(lambda x: int(x), num_list))

        new_col = [(dict_keys[i], dict_keys[i+1]) for i in range(0, len_dict_keys, 1) if i+1 < len(dict_keys)]

        i = 0
        while i < len(num_list):
            if num_list[i] > 0:
                xx = num_list[i] * (10**i)
                if xx in dict_keys:
                    result.append(dict1[xx])
                elif xx == abs((10**i) - (10**(i+1))):
                    result.append(dict1[10**i]+dict1[10**(i+1)])
                elif xx == (10**i) + 10**(i+1):
                    result.append(dict1[10**(i+1)]+dict1[10**i])
                else:
                    for cc in new_col:
                        if cc[0] < xx:
                            if xx == (abs(cc[0]-cc[1])):
                                result.append(dict1[cc[0]]+dict1[cc[1]])
                                break
                            elif xx == cc[0]+cc[1]:
                                result.append(dict1[cc[1]]+dict1[cc[0]])
                                break
                            elif xx > cc[1]:
                                if xx//(10**i) <=3 :
                                    result.append(dict1[10**i]*(xx//(10**i)))
                                    print(result)
                                    break
                            else:
                                if cc[0] < xx < cc[1]:
                                    if xx//(10**i) <=3 :
                                        result.append(dict1[10**i]*(xx//(10**i)))
                                        print(result)
                                    else:
                                        result.append(
                                            dict1[cc[0]]+dict1[10**i] *
                                            (abs    (xx-cc[0])//(10**i))
                                        )
            i +=1 

        result.reverse()
        return ''.join(result)
    
    def intToRoman2(self, num: int) -> str:
        dict1 = {1:["I"], 5:["V"], 10:["X"], 50:["L"], 100:["C"], 500:["D"], 1000:["M"]}
        result = []
        
        dict_keys = sorted(list(dict1.keys()))
        rev_dict_keys = dict_keys[::-1]
        num_list = [int(x) for x in str(num)]
        len_num = len(num_list)
        len_keys = len(dict_keys)

        i = 0
        while i < len_keys: 
            next_key = 0 if i+1 >= len_keys else dict_keys[i+1]
            dict1[dict_keys[i]].append((dict_keys[i], next_key))
            i +=1

        i = 0
        j = 0
        while j < len_num:
            print("Start ==> ", i, j, num_list[j])
            if i < len_keys:
                if num_list[j] > 0:
                    xx = num_list[j] * (10**((len_num-1)-j))
                    print(xx, rev_dict_keys[i], xx <= rev_dict_keys[i])

                    if xx in dict1:
                        result.append(dict1[xx][0])
                    else:
                        dd = abs(dict1[rev_dict_keys[i]][1][0] - dict1[rev_dict_keys[i]][1][1]) // (10**((len_num-1)-j))
                        
                        if xx == sum(dict1[rev_dict_keys[i]][1]):
                            result.append(
                                dict1[dict1[rev_dict_keys[i]][1][1]] + dict1[dict1[rev_dict_keys[i]][1][0]]
                            )

                            print("sum :: ", result)

                        elif xx == abs(dict1[rev_dict_keys[i]][1][0] - dict1[rev_dict_keys[i]][1][1]):
                            result.append(
                                dict1[dict1[rev_dict_keys[i]][1][0]] + dict1[dict1[rev_dict_keys[i]][1][1]]
                            )

                            print("subs :: ", result)
                        
                        else:
                                
                            print("="*10)
                            print("DD ",dd)
                            if xx >= rev_dict_keys[i]:
                                if dd > 4:
                                    print("grt then 4 -- 1 ", xx, dd, dict1[rev_dict_keys[i]][1][0], dict1[rev_dict_keys[i]][1][1])
                                    
                                    if xx == sum(dict1[rev_dict_keys[i]][1]):
                                        pass

                                    # result.append(
                                    #     dict1[rev_dict_keys[i]][1][0]
                                    # )
                                else:
                                    result.append(dict1[rev_dict_keys[i]][0] * num_list[j])
                            # else:
                            #     if xx == sum(dict1[rev_dict_keys[i]][1]):
                            #         result.append(
                            #             dict1[dict1[rev_dict_keys[i]][1][1][1]][0] + 
                            #             dict1[dict1[rev_dict_keys[i]][1][1][0]][1]
                            #         )
                            #     else:
                                    
                            #         if dd > 4:
                            #             print("grt then 4 -- 2 ", xx, dd, dict1[rev_dict_keys[i]][1][0], dict1[rev_dict_keys[i]][1][1])
                            #             # result.append(dict1[dict1[rev_dict_keys[i]][1][1][0]][0] + dict1[dict1[rev_dict_keys[i]][1][1][1]][0])
                            #         else:
                            #             pass
                            #             # result.append(dict1[rev_dict_keys[j]][0] * num_list[j])
                            print(dict1[rev_dict_keys[j]])
                            print("&"*10)
                j += 1
                i +=1 
            else:
                i +=1 
                continue
            
            
        print(result)
        # result.reverse()
        # return ''.join(result)

import time
x = [39,673, 979, 499, 3199]
ss = Solution()

start = time.time()
print(ss.intToRoman2(x[4]))
print(time.time() - start)
print("="*10)

# for i in x:
#     start = time.time()
#     print(ss.intToRoman(i))
#     print(time.time() - start)
#     print("="*10)

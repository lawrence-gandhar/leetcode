

class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))    

        last_words = word1[min_len:]+word2[min_len:]

        i = 0
        main_word = ""
        while i < min_len:
            main_word.append(word1[i]+word2[i])
            i += 1
        return ''.join(main_word)+last_words


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        li = []
        i = 0
        while i < max([len(word1), len(word2)]):

            print(i)
            try:
                li.append(word1[i])
            except:
                li.append(word2[i:])
                break
            try:
                li.append(word2[i])
            except:
                li.append(word1[i+1:])
                break
            
            i +=1

        return ''.join(li)
        
ss = Solution2()
print(ss.mergeAlternately(word1 = "ab", word2 = "pqdf"))
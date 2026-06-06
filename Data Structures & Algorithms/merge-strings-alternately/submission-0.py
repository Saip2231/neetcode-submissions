class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1,p2=0,0
        ans_str = ""
        while(p1 <len(word1) and p2<len(word2)):
            ans_str += word1[p1]
            ans_str += word2[p2]
            p1+=1
            p2+=1
            print(ans_str)
        if (p1<len(word1)):
            ans_str+=word1[p1:]
        else:
            ans_str+=word2[p2:]
        return (ans_str)

        
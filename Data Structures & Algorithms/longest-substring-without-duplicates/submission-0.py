class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0,0
        hash = dict()
        leng = 0
        max_leng = 0
        while(right <= len(s)-1):
            if s[right] not in hash:
                hash[s[right]] = 1+hash.get(s[right],0)
                right = right +1
                leng = leng + 1
            else:
                del hash[s[left]]
                left = left + 1
                leng = leng -1 
            max_leng = max(leng , max_leng)
            print(hash , max_leng)
        return max_leng
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list()
        i,j=0,0
        if (len(s)!=len(t)):
            return False
        for i in range (0 , len(s)):
            l1.append(s[i])
        for j in range(0,len(t)):
            if t[j] not in l1:
                return False
            l1.remove(t[j])
        return True

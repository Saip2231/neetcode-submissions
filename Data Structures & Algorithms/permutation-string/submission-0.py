class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1hash , s2hash = [0]*26 , [0]*26
        for i in range(len(s1)):
            s1hash[ord(s1[i]) - ord('a')] +=1
            s2hash[ord(s2[i]) - ord('a')] +=1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1hash[i] == s2hash[i] else 0)
        
        left = 0
        for right in range(len(s1) , len(s2)):
            if matches == 26: return True

            index = ord(s2[right]) - ord('a')
            s2hash[index] += 1
            if s1hash[index] == s2hash[index]:
                matches+=1
            elif s1hash[index] +1 == s2hash[index]:
                matches-=1


            index = ord(s2[left]) - ord('a')
            s2hash[index] -= 1
            if s1hash[index] == s2hash[index]:
                matches +=1
            elif s1hash[index] -1 == s2hash[index]:
                matches-=1
            left +=1 
        return matches == 26
            

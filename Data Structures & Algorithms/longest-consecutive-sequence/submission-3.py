class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0
        
        for n in  nums:
            #check if its the start of not
            if (n - 1) not in set1:
                length = 0
                while( n +length) in nums:
                    length +=1 
                longest = max(length , longest)
        return(longest)  
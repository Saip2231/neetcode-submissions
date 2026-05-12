class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        set1 = set(nums)
        longest = 0
        
        for n in set1:
            # Check if it's the start of a sequence
            if (n - 1) not in set1:
                length = 0
                while (n + length) in set1:
                    length += 1
                longest = max(length, longest)
        return longest
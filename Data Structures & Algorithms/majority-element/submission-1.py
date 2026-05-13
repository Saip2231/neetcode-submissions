class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for index, value in enumerate(nums):
            count_dict[value] = count_dict.get(value, 0) + 1
            if count_dict[value] >= len(nums) / 2:
                return value
        # max_key = max(countS, key=countS.get)
        # return(max_key)
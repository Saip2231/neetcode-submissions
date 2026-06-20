class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(cap):
            day = 1
            load = 0

            for w in weights:
                if load + w > cap:
                    day += 1
                    load = w
                else:
                    load += w 
            return day

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if days_needed(mid) <= days:
                right = mid
            else:
                left = mid + 1

        return left 
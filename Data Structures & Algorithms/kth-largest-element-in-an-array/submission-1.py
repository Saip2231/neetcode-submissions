class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # self.minheap , self.k = nums , k
        # heapq.heapify(self.minheap)
        # while(len(self.minheap) > k):
        #     heapq.heappop(self.minheap)
        # return self.minheap[0]

        k = len(nums)-k

        def quickselect(l,r):
            piv , p = nums[r] , l
            for i in range(l,r):
                if nums[i] <= piv:
                    nums[p] , nums[i] = nums[i] , nums[p]
                    p = p+1
            nums[p] , nums[r] = piv , nums[p]

            if p>k: return quickselect(l,p-1)
            elif p<k: return quickselect(p+1,r)
            else: return nums[p]
        
        return quickselect(0,len(nums)-1)
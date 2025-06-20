class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, result = collections.deque(), []

        for i, v in enumerate(nums):
            while deq and nums[deq[-1]] < v:
                deq.pop()

            deq.append(i)

            while deq[0] <= i - k:
                deq.popleft()
            
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result

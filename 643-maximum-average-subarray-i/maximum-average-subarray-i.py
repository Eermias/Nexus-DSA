class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        
        prev_sum = max_sum
        for i in range(1, len(nums) - k + 1):
            curr_sum = prev_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, curr_sum)
            prev_sum = curr_sum
        
        return max_sum / k

        


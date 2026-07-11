class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev = defaultdict(int)

        for i in range(len(nums)):
            other = target - nums[i]
            if other in prev:
                return [i, prev[other]]
            
            prev[nums[i]] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            curr = target - num
            if curr not in seen:
                seen[num] = i
            else:
                return [seen[curr], i]
        
        return 
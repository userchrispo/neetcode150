class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i = 0
        for num in nums:
            curr = target - num
            if curr not in map:
                map[num] = i
            else:
                return [map[curr],i]
            i += 1
        
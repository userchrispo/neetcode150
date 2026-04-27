class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = []

        for number in nums:
            if number not in map:
                map.append(number)
            else:
                return True
        
        return False
        
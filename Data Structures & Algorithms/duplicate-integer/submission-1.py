class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for int in nums:
            if int not in check:
                check.add(int)
            else:
                return True
        
        return False
        
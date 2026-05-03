from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        final = []

        for i in range(k):
            max_freq = -1
            most_freq_num = 0

            for num, freq in count.items():
                if freq > max_freq:
                    max_freq = freq
                    most_freq_num = num

            
            final.append(most_freq_num)
            del count[most_freq_num]
        
        return final



        # 1: 1 2:2  k = 2 

        
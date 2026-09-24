class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] += 1
        
        for item in count:
            freq[count[item]].append(item)
        
        for bucket in reversed(freq):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

                    

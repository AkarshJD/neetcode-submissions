class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #making the hash map with elements and their count
        countMap = {}
        # bucket for sort with count as index and lists of elements as elemtent in each array loc 
        # [[],[],[], ....]
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            countMap[i] = 1 + countMap.get(i,0)

        for n, c in countMap.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

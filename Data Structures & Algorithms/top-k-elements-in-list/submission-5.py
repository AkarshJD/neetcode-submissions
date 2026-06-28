class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #use HM to get the count
        #put it in the count of max elements

        #size of count array is max(ele)

        countMap = {}
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

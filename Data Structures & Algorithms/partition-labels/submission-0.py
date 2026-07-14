class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last index in s

        for i, c in enumerate(s):
            # even if it isnt, eventually we would have 
            # visited and updated to last occurance
            lastIndex[c] = i

        #Algo
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
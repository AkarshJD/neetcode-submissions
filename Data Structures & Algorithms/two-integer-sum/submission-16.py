class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # value -> index
        # 
        for i, n in enumerate(nums):
            diff = target - n
            #check if diff is in prevMap
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
            


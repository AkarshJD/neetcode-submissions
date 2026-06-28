class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # val -> index
        # we can return on request the comparing index and index in map

        for i, n in enumerate(nums):
            #nums[i] = target - nums[j]
            # first build the prev map
            diff = target - n
            #check if deff already in map
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return
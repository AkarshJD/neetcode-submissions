from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = reduce(lambda x, y: x ^ y, nums)
        return(result)
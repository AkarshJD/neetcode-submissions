class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. create empty hashmap
        2. Pass 1. Store everything
        3. Pass 2. search complements
        """

        #1. create hashmap
        indices = {}

        #2. Pass 1. Store everything
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [num_map[difference], i]  # Found the pair
            num_map[num] = i  # Store current number and its index
        
        return []  # This line should never be reached as per problem constraints

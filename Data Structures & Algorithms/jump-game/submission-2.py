class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Set goal to last index
        goal = len(nums) - 1

        # Go backwards through the list
        for i in range(len(nums) - 1, -1, -1):
            # If i can reach goal, move goal to i
            if i + nums[i] >= goal:
                goal = i

        # Check if start is reachable
        return goal == 0

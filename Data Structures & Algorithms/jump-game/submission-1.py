class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from the back
        # check if it can be reached by index i
        # decrement the target if it can be
        # if it reaches starting position return true
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
            
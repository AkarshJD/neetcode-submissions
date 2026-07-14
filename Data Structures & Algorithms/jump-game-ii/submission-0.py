class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        #What portion of the array is used for BFS currently
        l = r = 0 #window [0,0] [1,2] ...

        while r < len(nums) - 1:
            #who can jump the farthest
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
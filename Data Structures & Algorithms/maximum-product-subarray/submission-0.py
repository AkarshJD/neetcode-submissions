class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #0 -> [-1]
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0: #Edit in video - not needed but wks
                curMin, curMax = 1, 1
                continue
            
            tmp = curMax * n
            #What if we had -1, 8 curMax will be -8 so 8 itself is max
            #And in python 3 values for max works
            #Some langs dont allow it
            curMax = max(n * curMax, n * curMin, n)
            #Similar condition  - think for [-1, -8]
            #Also check for the bug - use temp(for curMax)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)

        return res

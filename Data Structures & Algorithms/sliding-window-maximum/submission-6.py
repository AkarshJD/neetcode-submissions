class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        curWin = []
        res = []
        # print(nums)
        for l in range(l,len(nums)-k+1):
            # print("l = ",l," r = ",l+k)
            curWin = nums[l:l+k]
            # print("curWin: ",curWin)
            res.append(max(curWin))
            l+=1
        return res
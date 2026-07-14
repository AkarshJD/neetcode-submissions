
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        maxL,maxR = 0,0

        for i in range(n):
            
            maxLeft[i]=maxL
            maxL = max(height[i],maxL)


        # print(maxLeft)
        for i in range(n-1,-1,-1):
            maxRight[i]=maxR
            maxR = max(height[i],maxR)
        # print(maxRight)
        for i in range(n):
            
            val = min(maxLeft[i],maxRight[i])-height[i]
            
            if(val>0):
                res +=val
            # print("Loop: ",i,"Val:",val,"Res:",res)

        return res

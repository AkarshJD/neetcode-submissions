class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #if first sorted number is non negative
            if a > 0:
                break

            #not reusing the same number before - duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            #two pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    #decrease our sum (coz sorted)
                    r -= 1
                elif threeSum < 0:
                    #increase sum
                    l += 1
                else:
                    #matches
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #when its same value
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


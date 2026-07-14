class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #Index and current subset as inputs
        def backtrack(i, subset):
            # gone through the entire array
            if i == len(nums):
                #To copy so that we dont want to overwrite
                res.append(subset[::])
                return

            #recursive case
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            #All subsets that don't include nums[i]
            #Duplicates will be right next to each other
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                #[1, 2, 2, 3]
            backtrack(i + 1, subset)

        backtrack(0 , [])
        return res        




class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()   # use a set instead of map()

        for ele in nums:
            if ele in seen:     # if we’ve seen it before, it's a duplicate
                return True
            seen.add(ele)       # otherwise add to set
        return False            # no duplicates found

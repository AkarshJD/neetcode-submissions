class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. Extreme Edge-Case Pruning using a Hash Map (Counter)
        # Python's collections.Counter is written in highly optimized C.
        # We handle zero and duplicates immediately to drastically reduce array size.
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            
        # Separate into unique negatives, positives, and handle zeros
        negatives = sorted([x for x in count if x < 0])
        positives = sorted([x for x in count if x > 0])
        res = []

        # Case 1: [0, 0, 0]
        if count.get(0, 0) >= 3:
            res.append([0, 0, 0])

        # Case 2: One zero, one negative, one positive (x + 0 + y = 0 -> y = -x)
        if 0 in count:
            for x in negatives:
                if -x in count:
                    res.append([x, 0, -x])

        # 2. Convert standard loops into localized set-lookups 
        # Dict lookup in Python is O(1) and implemented as a highly tuned C hash table.
        # We iterate over negative pairs to find a matching positive
        for i, x in enumerate(negatives):
            for j in range(i, len(negatives)):
                y = negatives[j]
                target = -(x + y)
                if target in count:
                    # If x == y, we need at least two copies of that negative number
                    if x == y and count[x] < 2:
                        continue
                    # Ensure target is valid (positive or handled zero)
                    if target > y: 
                        res.append([x, y, target])
                    elif target == y: # Guard rail if target managed to land exactly on y
                        break

        # 3. Iterate over positive pairs to find a matching negative
        for i, x in enumerate(positives):
            for j in range(i, len(positives)):
                y = positives[j]
                target = -(x + y)
                if target in count:
                    if x == y and count[x] < 2:
                        continue
                    if target < x:
                        res.append([target, x, y])
                    elif target == x:
                        break

        return res
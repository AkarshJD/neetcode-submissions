class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            #what if we run out of candidates or total > target
            if i==len(candidates) or total > target:
                return
            
            #include candidates[i]
            cur.append(candidates[i])
            #cant include the same element and new total
            dfs(i+1, cur, total + candidates[i])
            cur.pop()

            #skip candidates[i]
            #different from combination 1 which is just dfs
            while i+1 < len(candidates) and  candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur,total)

        dfs(0, [], 0)
        return res
from bisect import bisect_left, bisect_right

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        counts = Counter(nums)
        zero_count = counts.pop(0, 0)
        
        result = []
        append = result.append 
        
        if zero_count > 2:
            append([0, 0, 0])
            
        if not counts:
            return result
            
        unique = sorted(counts)
        counts_set = set(unique)
        
        for num in unique:
            if num < 0 and zero_count and -num in counts_set:
                append([num, 0, -num])
            
            if not num & 1: 
                candidate = -(num >> 1) 
                if candidate in counts_set and counts[candidate] > 1:
                    if num < candidate:
                        append([num, candidate, candidate])
                    else:
                        append([candidate, candidate, num])
        
        if len(unique) < 2:
            return result

        first_unique = unique[0]
        last_unique = unique[-1]
        a = -last_unique // 2 
        start = bisect_right(unique, a) if a > first_unique else 1
        
        a = -(first_unique // 2)
        stop = bisect_left(unique, a) if a < last_unique else len(unique) - 1
        
        for i in range(start, stop):
            num = unique[i]
            
            j = bisect_right(unique, -(num << 1)) if num < 0 else i + 1
            k = bisect_right(unique, -first_unique - num)
            
            for right in unique[j:k]:
                left = -num - right
                if left in counts_set:
                    append([left, num, right])
                    
        return result
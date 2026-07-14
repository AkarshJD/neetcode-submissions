class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        #loop through all intervals
        for i in range(len(intervals)):
            # if new interval end is less than interval start 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            #end
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            #could still overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)    
        return res

        

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #map adjacency list
        adj = {src:[] for src, dst in tickets}
        tickets.sort()

        #build adjacency list
        for src, dst in tickets:
            adj[src].append(dst)
        
        #dfs
        res = ["JFK"]
        def dfs(src):
            #base case
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            # Tricky part
            temp = list(adj[src])
            for i, v in enumerate(adj[src]):
                #Modify as we visit
                #but we cant really update as we iterate thoughg
                #rather that iterate through this use temp
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                #if not backtrack
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        # Initialize parent and rank arrays for Union-Find
        # parent of each node initialized to itself
        par = [i for i in range(N + 1)]  
        # rank[i] = size of the tree rooted at i
        rank = [1] * (N + 1)             

        # Find function with path compression
        # path compression: flatten the tree by making each node point 
        # directly to the root

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])    # path compression
            return par[n]

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:

                return False             

            # Union by rank: attach smaller tree under larger tree
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Iterate through edges and find the one that creates a cycle
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]          # this edge forms a cycle


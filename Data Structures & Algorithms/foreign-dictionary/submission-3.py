class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Create adj list
        adj = { c:set() for w in words for c in w}

        #for every single pair
        for i in range(len(words) - 1):
            #lets get every pair
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            #if prefix of the words is the exact same
            #but if invalid
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    #Char in word 2 comes after char in word 1
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} #False = visited, True = Current path
        #We are building in rev and later join
        res = []

        #Post order DFS
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            #for every char after this char
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        #Beginning at any single char - works
        #Coz we are starting from the reverse
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
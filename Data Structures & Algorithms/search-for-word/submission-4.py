class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        #position and current character in the word we are looking for
        def dfs(r, c, i):
            #We found the word
            if i == len(word):
                return True
            
            # 1. if out of bounds
            # 2. if we dont see the character we are looking for
            # 3. if we see it twice 
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            #once we see it - we found the char
            path.add((r, c))
            #is gonna return true if we find it while searching in all directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            #cleanup - coz we wont search the visited one again
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        
        return False

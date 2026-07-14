from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hash set
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set) # key = (r // 3, c // 3) -> set
                    
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rowMap[r] or
                    board[r][c] in colMap[c] or
                    board[r][c] in squareMap[( r // 3, c // 3)]):
                    return False
                else:
                    rowMap[r].add(board[r][c])
                    colMap[c].add(board[r][c])
                    squareMap[( r // 3, c // 3)].add(board[r][c])
        return True

        
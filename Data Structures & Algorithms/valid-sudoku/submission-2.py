class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hashyRows = defaultdict(set)
        hashyCols = defaultdict(set)
        hashySqr = defaultdict(set)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                
                if board[i][j] == '.':
                    continue

                val = board[i][j]

                sqr = (i // 3, j // 3)

                if val in hashyRows[i] or val in hashyCols[j] or val in hashySqr[sqr]:
                    return False
                
                hashyRows[i].add(val)
                hashyCols[j].add(val)
                hashySqr[sqr].add(val)
                    
        return True
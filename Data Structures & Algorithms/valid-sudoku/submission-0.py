class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hashyRows = defaultdict(set)
        hashyCols = defaultdict(set)
        hashySqr = defaultdict(set)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in hashyRows[i] or board[i][j] in hashyCols[j]:
                        return False
                    
                    hashyRows[i].add(board[i][j])
                    hashyCols[j].add(board[i][j])
                    
                    if j < 3:
                        if i < 3:
                            if board[i][j] in hashySqr[0]:
                                return False
                            hashySqr[0].add(board[i][j])
                        elif i < 6:
                            if board[i][j] in hashySqr[1]:
                                return False
                            hashySqr[1].add(board[i][j])
                        elif i < 9:
                            if board[i][j] in hashySqr[2]:
                                return False
                            hashySqr[2].add(board[i][j])
                    elif j < 6:
                        if i < 3:
                            if board[i][j] in hashySqr[3]:
                                return False
                            hashySqr[3].add(board[i][j])
                        elif i < 6:
                            if board[i][j] in hashySqr[4]:
                                return False
                            hashySqr[4].add(board[i][j])
                        elif i < 9:
                            if board[i][j] in hashySqr[5]:
                                return False
                            hashySqr[5].add(board[i][j])
                    elif j < 6:
                        if i < 3:
                            if board[i][j] in hashySqr[6]:
                                return False
                            hashySqr[6].add(board[i][j])
                        elif i < 6:
                            if board[i][j] in hashySqr[7]:
                                return False
                            hashySqr[7].add(board[i][j])
                        elif i < 9:
                            if board[i][j] in hashySqr[8]:
                                return False
                            hashySqr[8].add(board[i][j])

        return True
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        right = moves.count("R")
        left = moves.count("L")
        up = moves.count("U")
        down = moves.count("D")
        if right == left and up == down:
            return True
        return False
        
        """
        dic = {U:D, L:R, D:U, R:L}
        stack = []
        for i in moves:
            if 
        """
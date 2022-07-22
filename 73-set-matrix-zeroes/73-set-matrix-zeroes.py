class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        index = []
        
        for i in range(len(matrix)):
            
            row = matrix[i]
            
            if 0 in row:
                for j in range(len(row)):
                    if row[j] == 0:
                        index.append(j)
                matrix[i] = [0]*len(row)
                index = list(set(index))
                
    
        if index:
            for i in range(len(matrix)):
                row = matrix[i]
                
                if 0 not in row:
                    for j in index:
                        row[j] = 0
                

        return matrix
        
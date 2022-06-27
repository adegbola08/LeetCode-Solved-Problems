class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = {}
        
        for i in range(len(paths)):
            paths[i] = paths[i].split(" ")
        
            for j in range(1, len(paths[i])):
                l, r = paths[i][j].find("("), paths[i][j].find(")")
                
                if paths[i][j][l:r] not in duplicates:
                    duplicates[paths[i][j][l:r]] = [paths[i][0] + "/" +  paths[i][j][:l]]
                else:
                    duplicates[paths[i][j][l:r]].append(paths[i][0] + "/" +  paths[i][j][:l])
         
        res = []
        
        for i in duplicates:
            if len(duplicates[i]) > 1:
                res.append(duplicates[i])
        
        return res
                
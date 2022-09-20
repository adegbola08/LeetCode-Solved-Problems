class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        max_count = 1
        
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
                max_count = max(max_count, dic[word])
                
        result = []
        
        while max_count >= 1:
            temp = []
            
            for i in dic:
                if dic[i] == max_count:
                    temp.append(i)
            
            for i in sorted(temp):
                result.append(i)
                if len(result) == k:
                    return result
            
            max_count -= 1
            
        return result
        
        
            
        
        
        
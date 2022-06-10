class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for i in strs:
            count = [0]*26
            
            for j in i:
                count[ord(j) - ord("a")] += 1
            
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = [i]
            else:
                anagrams[key].append(i)
                
        return anagrams.values()
        
        
        """stack, result = set(), []
        
        for i in range(len(strs)):
            
            if strs[i] not in stack:
                stack.add(strs[i])
                temp = [strs[i]]
            
                if i+1 < len(strs):
                    for j in range(i+1, len(strs)):
                        
                        if "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
                            temp.append(strs[j])
                            stack.add(strs[j]) 
                
                result.append(temp)
                
        return result"""
                
            
            
                            
                        
                
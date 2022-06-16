class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            seen = set()
            r = i
            count = 0
            
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
                count += 1
            result = max(result, count)
            
        return result
            
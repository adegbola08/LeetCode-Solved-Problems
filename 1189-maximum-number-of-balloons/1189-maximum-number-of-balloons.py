class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        
        for ch in text:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        print(count)
        res = 0
        
        while True:
            for i in "balloon":
                if i in count and count[i] > 0:
                    count[i] -= 1
                else:
                    return res
            res += 1
        
        
        
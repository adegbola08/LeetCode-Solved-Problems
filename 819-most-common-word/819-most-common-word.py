class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        arr = paragraph.split(" ")
        
        dic = {}
        
        for i in range(len(arr)):
            temp = ""
            
            for j in arr[i]:
                if j.isalpha():
                    temp += j.lower()
                else:
                    break
            
            arr[i] = temp
            
            if arr[i] not in banned:
                if arr[i] not in dic:
                    dic[arr[i]] = 1
                else:
                    dic[arr[i]] += 1
        
        return max(dic, key=dic.get)
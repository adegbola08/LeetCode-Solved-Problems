class Solution:
    def replaceWords(self, dic: List[str], sentence: str) -> str:
        short = len(min(dic, key=len))
        long = len(max(dic, key=len))
        
        lst = sentence.split(" ")
        dic = set(dic)
        
        for i in range(len(lst)):
            cur = short
            while cur <= long:
                temp = lst[i][:cur]
                if temp in dic:
                    lst[i] = temp
                    break
                cur += 1
                
        return " ".join(lst)
        
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur = -1
        
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = cur
            if temp > cur:
                cur = temp
        
        return arr
        
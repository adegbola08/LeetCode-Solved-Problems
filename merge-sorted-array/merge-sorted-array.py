class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pos = 0
        
        for i in range(n,0,-1):
            nums1[-i] = nums2[pos]
            pos += 1
        
        return nums1.sort()
        
        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
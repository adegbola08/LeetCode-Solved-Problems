class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        if len(nums1) <= len(nums2):
            
            for elem in nums1:
                if elem in nums2:
                    result.append(elem)
                    nums2.remove(elem) 
            
        else:
            
            for elem in nums2:
                if elem in nums1:
                    result.append(elem)
                    nums1.remove(elem)
        
        return result
        
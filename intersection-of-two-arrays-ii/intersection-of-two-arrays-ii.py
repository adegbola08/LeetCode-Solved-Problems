class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import collections
        
        result = []
        
        if len(nums1) <= len(nums2):
            count = collections.Counter(nums2)
            
            for elem in nums1:
                if elem in count and count[elem] > 0:
                    result.append(elem)
                    count[elem] -= 1
                    
        else:
            count = collections.Counter(nums1)
            
            for elem in nums2:
                if elem in count and count[elem] > 0:
                    result.append(elem)
                    count[elem] -= 1
            
        
        return result
    
        
        """result = []
        
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
        
        return result"""
        
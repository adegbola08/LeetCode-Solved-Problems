class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        
        for i in range(len(nums1)):
            elem = nums1[i]
            pos = nums2.index(elem)
            for j in range(pos, len(nums2)):
                if nums2[j] > elem:
                    result[i] = nums2[j]
                    break
        
        return result
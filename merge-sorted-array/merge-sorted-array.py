class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if nums2:
            nums1[-n:] = nums2
            return nums1.sort()
        return nums1
       
        
        
        """
        pos = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                nums1[i] = nums2[pos]
                pos+=1
            i+=1
        return nums1.sort()
        """
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 <= nums2:
            lst = []
            for i in nums1:
                if i in nums2:
                    lst.append(i)
                    nums2.remove(i)
            return lst
        lst = []
        for i in nums2:
            if i in nums1:
                lst.append(i)
                nums1.remove(i)
        return lst
            
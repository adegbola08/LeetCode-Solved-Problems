class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left = 0
        right = len(height)-1
        
        while left != right:
            width = right - left
            
            if height[left] > height[right]:
                area = width * height[right]
                max_area = max(max_area, area)
                right -= 1
                
            else:
                area = height[left] * width
                max_area = max(max_area, area)
                left += 1
                
        return max_area
        
        
        """
        max_area = 0
        
        for i in range(len(height)-1):
            
            for j in range(i+1,len(height)):
                width = j - i
                tall = min(height[j],height[i])
                max_area = max(max_area, (width*tall))
        
        return max_area
        """
        
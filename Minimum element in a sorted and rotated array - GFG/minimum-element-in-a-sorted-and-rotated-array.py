#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        """arr.sort()
        return arr[0]"""
        
        left = 0
        right = n-1
        min_val = (arr[(right+left)//2])
        
        while left < right:
            possible_min = min(arr[left], arr[right])
            min_val = min(min_val, possible_min)
            left += 1
            right -= 1
            
        return min_val
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends
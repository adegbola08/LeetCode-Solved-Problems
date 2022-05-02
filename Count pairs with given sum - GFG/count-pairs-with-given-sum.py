#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        arr.sort()
        count = 0
        nums_seen = {}
        
        for i in range(len(arr)):
            if arr[i] > k:
                break
            
            if k-arr[i] in nums_seen:
                count += nums_seen[(k-arr[i])]
                
            if arr[i] in nums_seen:
                nums_seen[arr[i]] += 1
            else:
                nums_seen[arr[i]] = 1
            
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
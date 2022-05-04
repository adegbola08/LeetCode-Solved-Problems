#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max_sum = arr[-1]
        cur_max = 0
        
        for i in range(len(arr)):
            cur_max += arr[i]
            if cur_max > max_sum:
                max_sum = cur_max
            if cur_max <= 0:
                cur_max = 0
        return max_sum
        
        
        
        """max_sum = arr[-1]
        
        for i in range(len(arr)-1):
            if arr[i] > max_sum:
                max_sum = arr[i]
            temp_sum = arr[i]
            if arr[i] > 0:
                for j in range(i+1,len(arr)):
                    temp_sum += arr[j]
                    if temp_sum == 0:
                        break
                    max_sum = max(max_sum,temp_sum)
        return max_sum"""
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
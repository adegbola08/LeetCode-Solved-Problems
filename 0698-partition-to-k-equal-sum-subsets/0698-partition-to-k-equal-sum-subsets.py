from collections import defaultdict

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        subsets = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]

                    if backtrack(i + 1):
                        return True

                    subsets[j] -= nums[i]

                if subsets[j] == 0:
                    break

            return False

        return backtrack(0)

        

        
        


        
        
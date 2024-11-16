class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Conventional DP problem
        # The last state is at the last index, where its LIS have a length of 1.
        # Last the second-last index, the longest sequence would be either including just itself or 
        # including itself + the LIS of some later indecies that have a number greater than it.
        # Time: O(n^2)
        # Space: O(n)

        # Memoization initialization
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                # update only if eligible
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
        

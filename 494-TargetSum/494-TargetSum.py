class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # state will be (i, total_sum)
        dp = {} # a dictionary that stores the results of each state

        def backtrack(i, total):

            # base case, if reaches the end of the list
            # oob here since need to loop through all numbers
            if i == len(nums):
                # if the target sum is reached, there's one way to get the sum
                # else it will be 0
                return 1 if total == target else 0
            
            # base case if the current path is already explored
            if (i, total) in dp:
                return dp[(i, total)]
            
            # sum up the ways of getting the target sum
            # immediate return is nums[i], next state is (index+1, new_sum)
            dp[(i, total)] = backtrack(i+1, total+nums[i]) +backtrack(i+1, total-nums[i])
            return dp[(i, total)]
        
        return backtrack(0, 0)


# Time: O(n * sum(nums)) for caching
# Space: O(n * sum(nums))

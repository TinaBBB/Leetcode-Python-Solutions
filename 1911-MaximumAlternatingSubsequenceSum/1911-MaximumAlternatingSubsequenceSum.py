class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # DFS approach
        dp = {}

        def dfs(idx, ifeven):
            # Get oob base case
            if idx == len(nums):
                return 0
            
            # If already exists in the hashmap
            if (idx, ifeven) in dp:
                return dp[(idx, ifeven)]
            

            tmpTotal = nums[idx] if ifeven else (-1 * nums[idx])
            dp[(idx, ifeven)] = max(
                tmpTotal + dfs(idx+1, not ifeven),  # if choose the current number
                dfs(idx+1, ifeven) # if not choosing the current number
            )

            return dp[(idx, ifeven)]
        
        return dfs(0, True)
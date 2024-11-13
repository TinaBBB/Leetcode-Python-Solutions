class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(1)
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                # As long as reaching above and beyond
                goal = i

        return True if goal == 0 else False

        # # My original soltuion
        # # Time: O(n^2) ?
        # # Space: O(n)
        
        # # corner case if the list has length of 1
        # if len(nums) == 1:
        #     return True
        
        # # Initiate memoization dict
        # dp = {idx : False for idx in range(len(nums))}
        
        # # Start from last, work all the way to the initial index
        # for idx in range(len(nums)-1, -1, -1):
            
        #     action = nums[idx]

        #     # Loop through the max jump and gradually decrease
        #     # break found a way out
        #     for sub_act in range(action, -1, -1):
        #         if idx+sub_act >= len(nums) or dp.get(idx+sub_act):
        #             dp[idx] = True
        #             break
        # return dp[0]
        

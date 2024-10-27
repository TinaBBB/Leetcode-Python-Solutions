class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            print(n, rob1, rob2)
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
            print(rob1, rob2, temp)
        
        return rob2



        # """dfs approach, time limit exceeded : ("""

        # def dfs(curr_idx, last_robbed):
        #     # Base case, oob
        #     if curr_idx == len(nums):
        #         return 0
            
        #     # if we cannot rob due to last house was robbed
        #     if last_robbed:
        #         profit = dfs(curr_idx+1, False)
        #     else:
        #         profit = max(dfs(curr_idx+1, False), nums[curr_idx]+dfs(curr_idx+1, True))
            
        #     return profit
        
        # return dfs(0, False)

        

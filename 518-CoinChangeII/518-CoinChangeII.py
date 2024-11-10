class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # 3. Dynamic Programming solution with Memory of O(n)
        # Time complexity is still O(n*m)
        next_row = [0] * amount + [1]

        for row_idx in range(len(coins)-1, -1, -1):
            # Re-initiate the current row's values
            curr_row = [0] * amount + [1]
            curr_coin_val = coins[row_idx]
            
            for col_idx in range(amount-1, -1, -1):
                next_col_idx = col_idx+curr_coin_val
                # Get the combination of using the next coin
                curr_row[col_idx] = next_row[col_idx]

                # Get the combination if using the current coin
                if next_col_idx <= amount:
                    curr_row[col_idx] += curr_row[next_col_idx]
            next_row=curr_row.copy()
        
        return next_row[0]

        
        # # 2. Dynamic Programming solution
        # # Time: O(n*m)
        # # Memory: O(n*m)
        
        # # Construct a 2D array that stores the remaining amount (decending) as the columns, 
        # # and the coin amount (indecies) as the rows
        # dp = [[0] * amount + [1] for i in range(len(coins))]

        # # Start the bottom-up DP solution formation.
        # for row_idx in range(len(coins)-1, -1, -1):
        #     curr_coin_val = coins[row_idx]
        #     for col_idx in range(amount-1, -1, -1):
        #         next_col_idx = col_idx+curr_coin_val
        #         # Try to get result from the next coin, if choose not to select
        #         if row_idx+1 < len(coins):
        #             dp[row_idx][col_idx] += dp[row_idx+1][col_idx] 
        #         # Choose to select, same coin, different remaining value
        #         if next_col_idx <= amount:
        #             dp[row_idx][col_idx] += dp[row_idx][next_col_idx]
        # return dp[0][0]
        
        # 1. Memoization solution with dfs
        # EXCEEEDS TIME LIMITATION!!!! 
        # cache = {}

        # def dfs(index, total_amount):
        #     # base cases
        #     # check amount matches
        #     if total_amount == amount:
        #         return 1
        #     # check excessive amount
        #     if total_amount > amount:
        #         return 0
        #     # check if oob
        #     if index == len(coins):
        #         return 0
        #     if (index, amount) in cache:
        #         return cache[(index, amount)]
            
        #     # Choose the optimum solution between selecting the current coin 
        #     # or the next coin
        #     cache[(index, total_amount)] = dfs(index, total_amount+coins[index]) + dfs(index+1, total_amount)

        #     return cache[(index, total_amount)]
        
        # return dfs(0, 0)

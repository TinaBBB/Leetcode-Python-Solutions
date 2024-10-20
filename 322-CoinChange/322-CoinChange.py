class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # actions are coins
        reward_of_actions = 1
        # The optimal decisions to make at each state, which is the remaining amount of
        # money to make up to. Setting default value to be amount+1 since the most inefficient way is to 
        # add up 1s, amount+1 is not achievable based on the constraints. 
        opt_decisions = [amount+1]*(amount+1) 
        opt_decisions[0] = 0 # the most optimal soution to make at state 0 is 0, i.e., 0 coins to choose

        # Loop through all the possible states
        for state in range(len(opt_decisions)):
        # Loop through all the possible actions, skip the actions there state - action < possible states,
        # e.g., state=2, amount to make is 2, but action=5, in no cases need to make up amount of -3.
            for action in coins:
                # note the immediate rewarid is the same, which is 1
                next_state = state - action
                if next_state < 0: continue

                # Iteratively update the most optimal solution
                opt_decisions[state] = min(opt_decisions[state], reward_of_actions+opt_decisions[state-action])
        
        return opt_decisions[amount] if opt_decisions[amount] < amount +1 else -1

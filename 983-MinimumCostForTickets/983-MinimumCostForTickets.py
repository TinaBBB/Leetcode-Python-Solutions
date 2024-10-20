# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         actions=[1, 7, 30]
#         min_dollars = {day: float("inf") for day in days} # optimal solutions
#         # The base case is when at the last day, need to buy 1-day pass. 
#         min_dollars[days[-1]]=min(costs)
#         # rewards are costs

#         # Loop through days in reversed order, start from second last day state
#         for day_state_idx in range(len(days)-2,-1, -1):
#             day_state = days[day_state_idx]
#             # print("day_state:", day_state)
#             # print("curr_solution:", min_dollars)

#             # Loop through actions 
#             for pass_days_idx, pass_days in enumerate(actions):
#                 # Select possible state
#                 # next_state = find_next_day(day_state_idx, day_state + pass_days)
#                 covered_day = day_state + pass_days

#                 # Find the next day
#                 j = day_state_idx + 1
#                 next_state = None
#                 while j <= len(days)-1:
#                     if (days[j]) >= covered_day:
#                         next_state = days[j]
#                         break
#                     j+=1

#                 # print("action:", pass_days, "next_day:", day_state + pass_days) #, "next_state:", next_state)
#                 if next_state:
#                     # print(next_state)
#                     min_dollars[day_state]=min(min_dollars[day_state], costs[pass_days_idx]+min_dollars[next_state])
#                 else:
#                     min_dollars[day_state]=min(min_dollars[day_state], costs[pass_days_idx])
        
#         return min_dollars[days[0]]



"""DFS Solution"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_dollars = {}

        def dfs(days_idx):
            # base case, if gets oob
            if days_idx == len(days):
                return 0

            # Already computed scenario 
            if days_idx in min_dollars:
                return min_dollars[days_idx]

            # Not initiated
            min_dollars[days_idx] = float("inf")

            # Loop thorugh the action can be taken, as well as the cost
            for action, cost in zip([1, 7, 30], costs):
                next_day = days[days_idx] + action
                # Find the next feasible state
                # Find the next day

                j = days_idx
                # Note the max j we can get is len(days)
                while j <= len(days)-1 and days[j] < next_day:
                    j += 1
                
                # Get zero since j may become out of bound as the action covers all the days
                min_dollars[days_idx] = min(min_dollars[days_idx], cost+dfs(j))
            
            return min_dollars[days_idx]
        
        return dfs(0)
                




        

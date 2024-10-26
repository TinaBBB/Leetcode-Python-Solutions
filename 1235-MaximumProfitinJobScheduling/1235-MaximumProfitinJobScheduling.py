class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create sorted job information lists
        # Grouping together, and sort w.r.t the starting time.
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        # i is the current interval that we are at.
        def dfs(i):
            # base case, oob, can't get any profit
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # action: don't include element at index i, go to the next interval
            res = dfs(i+1)

            # action: include the current element
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            # intervals[i][2] is the profit, comparing the profit if not including
            # the current job, or the best job that comes after choosing the 
            # current job
            cache[i] = res = max(res, intervals[i][2] + dfs(j))

            return res

        return dfs(0)        
        
        
        

        """Dynamic Programming approach, but time limit exceeded : ( """
        # stages i are the startTime, this is where decisions need to be made, job i will be picked by default
        # states_i are the endTime, this is where the job ends, and helps to find the next job/stage
        # actions_i are 1. picking the job by default and 2. picking the next job j
        # reward_i: profit_i
        # next stage j: is basically actions_i, which determines the next job picked
        # decision*_i is the max_a profile_i + deicion*_j, note j is determined by a
            # s.t. stage_j >= state_i , i.e., start time should be >= current job's end time
        # Final function return should give the max values at all stages i. 
        stages_length = len(startTime)
        max_start_time = max(startTime)
        
        # Store the next feasible job start indecies for unique end times
        next_stage_dict = {}

        # Return a list of feasible jobs
        def binary_search(start_idx, min_endTime, end_idx=stages_length-1):
            
            # Already found the next starting indecies.
            if min_endTime in next_stage_dict:
                return next_stage_dict[min_endTime]

            # No next job can be triggered, we don't save it for space-saving reasons.
            if min_endTime>max_start_time:
                return [stages_length]

            # Use binary search to find the next best job indecies
            mid_idx = (start_idx + end_idx) // 2

            while start_idx < end_idx:
                if min_endTime <= endTime[mid_idx]:
                    end_idx = mid_idx
                else:
                    start_idx = mid_idx + 1
            return list(range(start_idx, stages_length))


        # Also assuming that the startTime list is sorted
        profit_chart = {time_idx: float("-infinity") for time_idx in range(stages_length)}
        profit_chart[stages_length] = 0 #profit at oob stage is 0


        # Loop through stages from the last start time
        for stage_i in range(stages_length-1, -1, -1):
            ending_time_i = endTime[stage_i]
            profit_i = profit[stage_i]

            # Find feasible next stage_j 
            # next_stages_j = binary_search(stage_i+1, ending_time_i)
            next_stage_j = bisect.bisect_left(startTime, ending_time_i, stage_i+1, stages_length)
            for stage_j in list(range(next_stage_j, stages_length+1)):
                profit_chart[stage_i] = max(profit_chart[stage_i], profit_i + profit_chart[stage_j])

            # break
        return max(profit_chart.values())

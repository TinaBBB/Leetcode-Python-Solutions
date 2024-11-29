class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom-up solution
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum//2

        # Stands for remaining  sum, last column is when remaining sum = 0, means a match
        last_row = [False for sum in range(target_sum)] + [True]
        for idx in range(len(nums)-1, -1, -1):
            new_row = [False for sum in range(target_sum)] + [True]
            for curr_sum in range(target_sum-1, -1, -1):

                remain_sum = target_sum - curr_sum
                # Does not have the option to be selected
                if nums[idx] > remain_sum:
                    new_row[curr_sum] = last_row[curr_sum]
                    continue
                
                
                # Choose between select the current number or not
                new_row[curr_sum] = last_row[curr_sum] or last_row[curr_sum+nums[idx]]
            last_row = new_row
        
        return last_row[0]
                
        # # Top-down solution, very slow.
        # # Time: O()
        # # Space: O()
        # total_sum = sum(nums)
        # if total_sum % 2 != 0:
        #     return False

        # target_sum = sum(nums)/2
        # cache = {} # (idx, curr_sum):

        # def dfs(idx, curr_sum):
        #     if idx >= len(nums) or curr_sum > target_sum:
        #         return False
        
        #     if curr_sum == target_sum:
        #         return True
        
        #     if (idx, curr_sum) in cache:
        #         return cache[(idx, curr_sum)]

        #     if_partition = dfs(idx+1, curr_sum) or dfs(idx+1, curr_sum + nums[idx])
        #     cache[(idx, curr_sum)] = if_partition
        #     return if_partition

        # return dfs(0, 0)



        # Previous solution
        # # If odd total sum
        # if sum(nums) % 2:
        #     return False
        # # Keeps the set of totals 
        # dp = set()
        # dp.add(0)
        # target = sum(nums) // 2

        # # Looping through each number within the nums set
        # for i in range(len(nums)-1, -1, -1):
        #     nextDP = set()
        #     for t in dp:
        #         if (t + nums[i]) == target:
        #             return True
        #         # Adding numbers together
        #         nextDP.add(t + nums[i])

        #         # update the total set 
        #         nextDP.add(t)
        #     dp = nextDP
        

        # return True if target in dp else False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # If odd total sum
        if sum(nums) % 2:
            return False

        # Keeps the set of totals 
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        # Looping through each number within the nums set
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                # Adding numbers together
                nextDP.add(t + nums[i])

                # update the total set 
                nextDP.add(t)
            dp = nextDP
        

        return True if target in dp else False
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Time: O(n) to iterate through the numbers 2 times
        # Space: O(1) since just storing the two variables rob1 and rob2
        if len(nums) == 1:
            return nums[0]
        
        # This is the logic for the house robber.
        def helper(nums):
            rob1, rob2 = 0,0

            for n in nums:
                newRob = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        
        # Here we just need to consider the sub problem of robbing the houses excluding either the
        # beginning or the ending houses.
        return max(helper(nums[1:]), helper(nums[:-1]))
        

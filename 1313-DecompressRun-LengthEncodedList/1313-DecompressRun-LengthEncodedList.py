class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        results = []

        for i in range(len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i+1]

            results += [val]*freq

        return results

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []

        total = 0

        for weight in w:
            total += weight

            self.prefix_sums.append(total)
        
        self.total = total
        # print(self.total, self.prefix_sums)
        

    def pickIndex(self) -> int:
        # [1,2,3] --> [1,3,7] --> 4
        # First roll a number
        target = random.uniform(0, self.total)

        l=0 
        r=len(self.prefix_sums)

        # moving left and right down, left will be the solution we want to return
        while l < r:
            mid = (l+r) // 2

            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                # want to set equal, because the mid could be the right solution
                r = mid 
            
        return l

# INIT --> T: O(N) for , S: O(N)
# pickIndex --> T: log(N) to bninary search, O(1) as just storing left and right pointers



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

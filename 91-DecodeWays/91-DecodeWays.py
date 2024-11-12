class Solution:
    def numDecodings(self, s: str) -> int:

        # DP solution
        # Time O(n)
        # Space O(n)
        dp = {len(s):1} #set base case, where if reaches the end, it's 1 way to decode


        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 
            else:
                dp[i] = dp[i+1]
            
            if (i+1 <len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]


        # # Recursive solution
        # # Time O(n)
        # # Space O(n)
        # dp = {len(s):1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
            
        #     # Choose to decode one string
        #     res = dfs(i+1)
        #     if (i+1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
        #         res += dfs(i+2)
            
        #     dp[i] = res
        #     return res
        
        # return dfs(0)


        # # Brute force dfs approach, time limit exceeded!!!!
        # # Creat the mapping dict
        # decode_dict = {
        #     str(i): char
        #     for i, char in zip(range(1, 27), string.ascii_uppercase)

        # }

        # def dfs(idx_pointer, remain_str):
        #     # base case, only one string remains
        #     if len(remain_str)-idx_pointer == 1:
        #         if decode_dict.get(remain_str):
        #             return 1
        #         else: return 0
            
        #     # base case, when unable to encode
        #     if not decode_dict.get(remain_str[:idx_pointer+1]):
        #         return 0
            
        #     # Decode based on idx pointer
        #     if idx_pointer == 0:
        #         # choose to encode the first digit or first two digit
        #         return dfs(0, remain_str[1:]) + dfs(1, remain_str)
            
        #     if idx_pointer == 1:
        #         return dfs(0, remain_str[2:])
        
        # return dfs(0, s)        

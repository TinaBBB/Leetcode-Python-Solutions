class Solution:
    
    # LCS solution, of string itself, and its reverse
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
        
    # Time: O(mn) to compute the grid
    # Memory: O(mn) to store the grid    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            # oob have 0 paddings
            dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

            # Loop through rows from the bottom and columns from the right
            for row_idx in range(len(text1)-1, -1, -1):
                for col_idx in range(len(text2)-1, -1, -1):
                    # match, go diagonal
                    if text1[row_idx] == text2[col_idx]:
                        dp[row_idx][col_idx] = 1 + dp[row_idx+1][col_idx+1]
                    # not match, check max of right and bottom values
                    else:
                        dp[row_idx][col_idx] = max(
                            dp[row_idx][col_idx+1], dp[row_idx+1][col_idx]
                            )

            return dp[0][0]


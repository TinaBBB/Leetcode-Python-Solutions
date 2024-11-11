class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0

        # Loop through each index i to try to find the palindrome
        for i in range(len(s)):

            # odd-number palindrome, e.g., "aba"
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen: # check longest
                    result = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1

            # even-number palindrome, e.g., "bb"
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen: # check longest
                    result = s[l:r+1]
                    resLen = r-l+1

                l-=1
                r+=1
            
        return result

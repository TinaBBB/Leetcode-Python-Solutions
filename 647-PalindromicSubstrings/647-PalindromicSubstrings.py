class Solution:
    def countSubstrings(self, s: str) -> int:

        result = 0 

        # loop through the string
        for idx in range(len(s)):
            
            # odd-length substrings
            l = r = idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result +=1
                l -= 1
                r += 1
            
            # even-length substrings
            l, r = idx, idx+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result +=1
                l -= 1
                r += 1
        
        return result

        
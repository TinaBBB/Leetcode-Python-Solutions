class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # A 2-dimensional cache to store the returns.
        cache = [[float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]

        # Fill in the base cases
        # when one of the strings is empty, the operations to make is the length of the string.

        # base case when word2 substring is empty
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1) - i
        
        # base case when word1 substring is empty
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):

                # if matching
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        

        return cache[0][0]

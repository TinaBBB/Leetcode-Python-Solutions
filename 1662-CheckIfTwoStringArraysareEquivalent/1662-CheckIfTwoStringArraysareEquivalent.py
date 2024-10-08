class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = 0   # word index in both arrays
        i = j = 0    # character index in both arrays

        while w1 < len(word1) and w2 < len(word2):
            # false case
            if word1[w1][i] != word2[w2][j]:
                return False
            
            # increase the pointers
            i += 1
            j += 1

            # Move word index pointers up
            if i == len(word1[w1]):
                w1 += 1
                i = 0
            if j == len(word2[w2]):
                w2 += 1
                j = 0
            
        # Finished loop but one is longer than the other
        if w1 != len(word1) or w2 != len(word2):
            return False
        
        return True

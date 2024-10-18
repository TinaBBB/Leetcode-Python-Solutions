class Solution:
    def compressedString(self, word: str) -> str:
        return_str = ""
        max_repeat = 9 


        count = 0
        for idx in range(len(word)):
            curr_val = word[idx]

            count += 1

            # Record count
            if idx == len(word)-1 or word[idx+1] != word[idx] or count == max_repeat:
                return_str+=f"{count}{curr_val}"
                count = 0 
        
        return return_str

            
        

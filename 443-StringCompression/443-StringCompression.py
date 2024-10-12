class Solution:
    def compress(self, chars: List[str]) -> int:
        # Need to modify and append the new result in place. 
        # freq_count = dict()
        len_to_loop = len(chars)

        if len(chars) == 1:
            return 1

        count = 0
        # Need to loop through the original list of characters O(N)
        for index in range(len_to_loop):
            # Count frequency of the character
            curr_char = chars.pop(0)
            count += 1
            print(curr_char)

            # Append results
            if (index < len_to_loop-1 and curr_char != chars[0]) or (index == len_to_loop-1):
                chars.append(curr_char)
                if count != 1:
                    chars.extend(list(str(count)))
                count = 0
        
        return len(chars)

        

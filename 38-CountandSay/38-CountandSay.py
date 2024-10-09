class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        # Get the compressed encoded string function.
        def get_compressed_str(last_string):
            curr_string = ""
            start_p, end_p = 0, 0

            # Iterate through the last string
            while end_p < len(last_string):
                
                # recording point, append frequency and value
                if end_p == len(last_string)-1 or last_string[end_p] != last_string[end_p+1]:
                    curr_string+=str(end_p-start_p+1)+str(last_string[end_p])
                    # move up into the next starting point
                    start_p = end_p = end_p+1
                else:
                    end_p += 1

            return curr_string

        # Loop through all the previous numbers.
        last_str = "1"
        for index in range(2, n+1):
            # print(index, "last_str:", last_str)
            curr_str = get_compressed_str(last_str)
            # print(index, "curr_str:", curr_str)
            if index < n:
                last_str = curr_str
            else:
                return curr_str

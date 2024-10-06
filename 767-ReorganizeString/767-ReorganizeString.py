class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        The idea is to insert the most frequent, non-previously used character from a 
        frequency hashmap. In order to get the character that has the most frquency,
        we use a min heap - modified max heap version in Python, as Python does not have built-in
        maxheap library. Specifically, instead of using the character's original frequency number, we
        use the corresponding negative value of the frequencies. 
        Base case:
            The valid string will not be formed if the most frequent item's frequency is > math.ceil(len(s)/2).
            e.g., len(s)=3, "aab", the most frequent element can only be placed at [0, 2], same with len(s) = 4
            when len(s)=5 or len(s)=6, the most frequent element can only have a frequency of 3, placing at [0, 2, 4].

        At iterations:
            * At each iteration, pop the most frequency character from the minheap and append it to the result string.
            * Push the previous value into the minheap list
            * Modify the frequency of the popped item, i.e., increase 1 as it's negative value, set it as the prev parameter if 
            the value is not 0.

        """

        from collections import Counter
        
        """
        Initialization.
        """
        # Count the frequency of the string values.
        freq_map = Counter(s)
        # print(freq_map)

        # Create the min heap by using the frequency heap.
        max_heap = [[-freq, char] for char, freq in freq_map.items()] #O(n)
        heapq.heapify(max_heap)
        # print(max_heap)

        # The previous inserted value, and return string initiation
        prev_val = None
        result_str = ""

        """
        Iteration
        """
        # Enter the loop if there's still some characters remaining to be appended
        while max_heap or prev_val:
            
            # Popping the most frequent value and appending to result
            cur_freq, cur_val = heapq.heappop(max_heap)
            # Base check, that would happen in the first iteration:
            if -cur_freq > math.ceil(len(s)/2):
                return ""
            result_str+=cur_val
            
            # Free up the prev_val parameter
            if prev_val:
                heapq.heappush(max_heap, prev_val)
                prev_val = None

            # Set the current value to be the prev_val if there's still remaining counts
            if cur_freq < -1:
                prev_val = [cur_freq+1, cur_val]

        return result_str 
        

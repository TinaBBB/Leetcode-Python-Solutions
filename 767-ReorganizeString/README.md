### Descriptions 
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 
Example 1:
Input: s = "aab"
Output: "aba"
Example 2:
Input: s = "aaab"
Output: ""

 
Constraints:


	1 <= s.length <= 500
	s consists of lowercase English letters.


### Solution Explanation
[Referenced Solution](https://leetcode.com/problems/reorganize-string/description/)

This solution attempts to reorganize the input string `s` such that no two adjacent characters are the same. It leverages a **max-heap** (simulated using Python's `heapq` with negative frequencies) to repeatedly pick the character with the highest remaining frequency. The approach ensures that at each step, the most frequent character is chosen, and the previously used character is pushed back into the heap (if it still has remaining frequency) to be used again later. The key idea is that the character with the highest frequency is used strategically to avoid consecutive placements.

#### Steps:
1. **Count character frequencies**: A frequency map (`freq_map`) of the characters in `s` is created using `Counter`.
2. **Max-heap creation**: The character frequencies are pushed into a max-heap (simulated using a min-heap with negative frequencies).
3. **Iterative reorganization**:
   - Pop the character with the highest frequency from the heap and add it to the result.
   - If there is a "previous" character stored (one that was used in the last step), push it back into the heap for reuse.
   - Update the "previous" character as the current character if it still has remaining frequency after being used.
4. **Return the result**: If the max character frequency is more than half the length of `s`, it's impossible to reorganize, so return an empty string. Otherwise, return the successfully built string.

### Time Complexity:

1. **Frequency Counting**: Building the frequency map takes \( O(n) \), where \( n \) is the length of the string `s`.
2. **Heap Construction**: Constructing the heap takes \( O(d log d) \), where \( d \) is the number of distinct characters (since we push `d` elements into the heap).
3. **Heap Operations in the While Loop**: In the worst case, we pop from the heap and push back into it for every character in `s`. Each pop or push operation takes \( O(log d) \), so iterating over all characters takes \( O(n log d) \).

Since \( d <= n \) (the number of distinct characters is at most the total number of characters), the heap operations dominate the complexity.

**Overall Time Complexity**:  
- \( O(n log d) \), where \( n \) is the length of the string and \( d \) is the number of distinct characters.

### Space Complexity:

1. **Frequency Map**: The frequency map takes \( O(d) \) space, where \( d \) is the number of distinct characters.
2. **Max-Heap**: The heap stores at most \( d \) elements, so it takes \( O(d) \) space.
3. **Result String**: The result string will have length \( O(n) \).
4. **Auxiliary Space for Variables**: Other variables like `prev_val` and counters take constant space.

**Overall Space Complexity**:  
- \( O(n + d) \), where \( n \) is the length of the string and \( d \) is the number of distinct characters. In the worst case, \( d \) could be \( O(n) \), so the space complexity simplifies to \( O(n) \).

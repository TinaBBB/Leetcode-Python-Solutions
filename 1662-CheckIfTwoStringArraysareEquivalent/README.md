Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false


Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true


 
Constraints:


	1 <= word1.length, word2.length <= 103
	1 <= word1[i].length, word2[i].length <= 103
	1 <= sum(word1[i].length), sum(word2[i].length) <= 103
	word1[i] and word2[i] consist of lowercase letters.


## Problem: Compare Two Lists of Strings

This solution compares two lists of strings (`word1` and `word2`) to determine if their concatenated versions are equivalent. The idea is to simulate the concatenation of the strings without actually concatenating them, by iterating through both lists and comparing character by character.

### Time Complexity:
Let \( n_1 \) be the total number of characters in `word1` and \( n_2 \) be the total number of characters in `word2`.

- The algorithm traverses each character from both `word1` and `word2` once.
- Hence, the total time complexity is \( O(\max(n_1, n_2)) \).

#### Explanation:
Each character in `word1` and `word2` is visited exactly once during the loop, and both pointers `i` and `j` move to the next character after each comparison. Therefore, the time complexity is proportional to the sum of the lengths of all the strings in both lists.

### Space Complexity:
- The space complexity is \( O(1) \) because only a constant amount of extra space is used to store the pointers `w1`, `w2`, `i`, and `j`. No additional data structures are used, and the input lists are not modified.

### Summary:
- **Time complexity**: \( O(\max(n_1, n_2)) \), where \( n_1 \) is the total number of characters in `word1` and \( n_2 \) is the total number of characters in `word2`.
- **Space complexity**: \( O(1) \), since the solution only uses a fixed amount of extra space.

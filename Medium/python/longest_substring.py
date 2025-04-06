class LongestSubstring():
    """
    Solution for leetcode problem: 3. Longest Substring Without Repeating Characters

    stats: 
    Runtime: Beats 91.46%
    Memory: Beats 15.09%
    """
    def solution(self, s):
        """
        Loops through each character and documents its value in a key-value dictionary.
        If a character already exists in the dictionary the keys index is stored in repeated_letter_index.
        repeated_letter_index works as a pointer, the substring must start after this pointer to not contain 2 of the same character.
        Each substring [repeated_letter_index + 1: i + 1] is tested against longest_substring to see if it's longer,
        and it that case it replaces the previous value.

        Args:
            s (string): The string to find the longest substring in.

        Returns:
            int: Length of the longest substring.
        """
        substring_indexes = {}
        longest_substring = ""
        repeated_letter_index = -1

        for i in range(len(s)):
            if s[i] in substring_indexes and substring_indexes[s[i]] > repeated_letter_index:
                repeated_letter_index = substring_indexes[s[i]]
            substring_indexes[s[i]] = i

            if len(s[repeated_letter_index + 1:i + 1]) > len(longest_substring):
                longest_substring = s[repeated_letter_index + 1:i + 1]
        
        return len(longest_substring)

#Tests
if __name__ == "__main__":
    s1 = "amioujma"

    longest_substring = LongestSubstring()
    
    print(longest_substring.solution(s1))

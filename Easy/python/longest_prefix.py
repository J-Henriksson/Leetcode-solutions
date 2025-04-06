class LongestPrefix():

    def longest_common_prefix(self, strs):
        """Brute force method (kind of) goes through each letter in the first string of the list and checks if every other entry contains the same letter at the same position.
        This process is continued until a letter that that doesn't fulfill this is found or until the last word si reached. In which case the letter being looped through is added to the list of
        letters to be returned as a string.

        Analysis: Pretty straightforward "brute force" approach, I mean it works but still not very cool or elegant. Time complexity of O(n^2).
        Runtime: Beats 7.73% :(
        Memory: Beats 91.75% 

        Args:
            strs (list): A list containing the strings where the longest prefix should be found.

        Returns:
            string: The common prefix (if there is any, otherwise an empty string)
        """
        if len(strs) == 1:
            return strs[0]

        prefix_letters = []
        for letter in range(1, len(strs[0]) + 1):
            for word in range(1, len(strs)):
                if strs[0][0:letter] != strs[word][0:letter]:
                    break
                elif word == len(strs) - 1:
                    prefix_letters.append(strs[0][letter - 1])
        
        return "".join(prefix_letters)
    



    def longest_common_prefix_lexicographical_order(self, strs):
        """Cool method that starts by sorting the list of words in lexicographical  order (alphabetical order) and then only compares the difference between the first and last words.
        since if the first and last word share the same first letters, all other letters in the list must share these as well.

        Analysis: Overall really dope and elegant solution, time complexity is O(n). Only real caveat of coming up with this solution is being familiar with how the sort method works for strings.
        Runtime: Beats 100%
        Memory: Beats 91.75% 
        Fuck yeah.

        Args:
            strs (list): A list containing the strings where the longest prefix should be found.

        Returns:
            string: The common prefix (if there is any, otherwise an empty string)
        """
        strs.sort()

        for letter in range(1, len(strs[0]) + 1):
            if strs[0][0:letter] != strs[len(strs) - 1][0:letter]:
                return strs[0][0:letter - 1]
            elif letter == len(strs[0]):
                return strs[0]
        return ""
                
    

if __name__ == "__main__":
    strs = ["gaybba", "gay"]
    longest_prefix = LongestPrefix()
    prefix = longest_prefix.longest_common_prefix_lexicographical_order(strs)
    print(prefix)
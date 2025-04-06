class IndexOfFirstOccurrence():

    def needle_in_haystack(self, haystack, needle):
        """This method just iterates through each letter in the haystack, if the letter at the index matches the first letter of the needle, the part of the haystack that would contain the needle
        starting from the index is checked to see if it matches the needle. If the length needed to find the needle in the haystack from where the index's position is too small the loop breaks.

        Analysis: Overall a rly easy problem with a very straightforward approach to solving it efficiently. The time complexity is just O(n).
        Runtime: Beats 100%
        Memory: Beats 81.22% 

        Args:
            haystack (_type_): String representing the haystack to search through.
            needle (_type_): String representing the needle to look for.

        Returns:
            int: Index of starting letter of the needle or if not found -1.
        """
        index = 0
        while index <= len(haystack) - len(needle):
            if index + len(needle) > len(haystack):
                break
            if haystack[index] == needle[0]:
                if haystack[index: index + len(needle)] == needle:
                    return index
            index +=1
        return -1

if __name__ == "__main__":
    index = IndexOfFirstOccurrence()
    print(index.needle_in_haystack("dewdwedsadsaddddddddd", "sad"))
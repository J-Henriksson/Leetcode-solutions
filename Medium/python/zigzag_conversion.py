class ZigzagConversion():
    
    def convert(self, s: str, num_rows: int) -> str:
        #Make a list of strs where each str represents a row. Append each character to a string and keep moving the index up and down from 0-7. Then merge the strings.
        if num_rows == 1:
            return s
        rows = [""] * num_rows
        j = 0
        index = 1
        for i in range(len(s)):
            rows[j] += s[i]
            j += index
            if j == len(rows) - 1 or j == 0:
                index *= -1
        return "".join(rows)


if __name__ == "__main__":
    converter = ZigzagConversion()
    s = "PAYPALISHIRING"
    s2 = "AB"
    print(converter.convert(s,3))
    print(converter.convert(s,4))
    print(converter.convert(s2,1))
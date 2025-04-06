class IntegerToRoman():

    int_to_roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
    }
    
    def integer_to_roman(self, num):
        """Takes an integer under 4000 and converts it to roman numeral form.

        Analysis: Pretty intuitive and straight forward solution.
        Runtime: Beats 87.04%
        Memory: Beats 70.64%

        Args:
            num (int): Integer to be converted to roman numerals. 

        Returns:
            roman (string): String representing the integer in roman numeral form.
        """
        sum = num
        roman = ""
        for number in self.int_to_roman:
            roman += self.int_to_roman[number] * (sum // number)
            sum -= (sum // number) * number
            if sum == 0:
                return roman

if __name__ == "__main__":
    integer_to_roman = IntegerToRoman()

    print(integer_to_roman.integer_to_roman(3749))
    print(integer_to_roman.integer_to_roman(58))
    print(integer_to_roman.integer_to_roman(1994))
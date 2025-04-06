class DivideTwoIntegers():

    def divide_two_integers(self, dividend, divisor):
        """Method that performs division without using the division or multiplication operator. Does this using bit shifts, i.e. converting to binary form and adding another bit
        (aka "multiplying" by 2). basically we move 1 one bit at the time (multiplying by 2) until we're one bit (one multiplication of 2) away from exceeding the size of the dividend.
        Then we subtract what we have from the dividend and repeat the process on the remainder. We do this until the remainder becomes less than the divisor, thus we get the integer
        quotient of the division.
        So essentially we boil down each division into this form: dividend/divisor = (exponent * divisor) +remainder / divisor.
        Where the exponent is some exponent of 2.

        Analysis: Overall a pretty dope solution that intuitively solves the problem.
        Runtime: Beats 100%
        Memory: Beats 86.06%

        Args:
            dividend (int): Dividend of the division, duuuuh.
            divisor (int): Divisor of the division.

        Returns:
            int: quotient, the integer result of the division, rounded down.
        """
        abs_divisor = abs(divisor)
        remainder = abs(dividend)
        exponent = 1
        quotient = 0

        while remainder >= abs_divisor:
            if abs_divisor << 1 > remainder: 
                remainder -= abs_divisor
                abs_divisor = abs(divisor)
                quotient += exponent
                exponent = 1
            else:
                abs_divisor = abs_divisor << 1
                exponent = exponent << 1   

        if (dividend < 0) != (divisor < 0):
            if quotient > 2**31:
                return -2**31
            return -quotient
        if quotient > 2**31 - 1:
            return 2**31 - 1
        return quotient
        

if __name__ == "__main__":
    divide_two_integers = DivideTwoIntegers()
    print(divide_two_integers.divide_two_integers(10, 5))
    print(divide_two_integers.divide_two_integers(10, -3))
    print(divide_two_integers.divide_two_integers(10, 10))
import math

class IfDigitEqual():
    def has_same_digits(self, s: str) -> bool:
        while len(s) != 2:
            for i in range(len(s)):
                if i == len(s) - 1:
                    s = s[:len(s) - 1]
                else:
                    s = s[:i] + str((int(s[i]) + int(s[i + 1])) % 10) + s[i + 1:]
        if s[0] == s[1]:
            return True
        return False
    
    def has_same_digits_better(Self, s: str) -> bool:
        sum_left, sum_right = 0,0
        for i in range(len(s) - 1):
            sum_left += math.comb(len(s) - 2, i) * int(s[i])
            sum_right += math.comb(len(s) - 2, i) * int(s[i + 1])
        return (sum_left % 10) == (sum_right % 10)
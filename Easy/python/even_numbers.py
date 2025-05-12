from typing import List
from collections import defaultdict 

class EvenNumbers(object):
    def find_even_numbers(self, digits: List[int]) -> List[int]:
        occurrences = [0] * 10
        for digit in digits:
            occurrences[digit] += 1
        result = []
        
        for digit_1 in (2, 4, 6, 8, 0):
            if occurrences[digit_1] != 0:
                occurrences[digit_1] -= 1
                for digit_2 in range(10):
                    if occurrences[digit_2] != 0:
                        occurrences[digit_2] -= 1
                        for digit_3 in range(1, 10):
                            if occurrences[digit_3] != 0:
                                result.append(digit_3 * 100 + digit_2 * 10 + digit_1)
                        occurrences[digit_2] += 1
                occurrences[digit_1] += 1
        result.sort()
        return result
    
    def find_even_numbers_dict(self, digits: List[int]) -> List[int]:
        
        digits.sort()
        occurrences = defaultdict(int)
        for digit in digits:
            occurrences[digit] += 1
        result = []

        for digit_3 in occurrences:
            if digit_3 != 0 and occurrences[digit_3] != 0:
                occurrences[digit_3] -= 1
                for digit_2 in occurrences:
                    if occurrences[digit_2] != 0:
                        occurrences[digit_2] -= 1
                        for digit_1 in occurrences:
                            if digit_1 % 2 == 0 and occurrences[digit_1] != 0:
                                result.append(digit_3 * 100 + digit_2 * 10 + digit_1)
                        occurrences[digit_2] += 1
                occurrences[digit_3] += 1
        return result

    
if __name__ == "__main__":
    even_numbers = EvenNumbers()
    digits = [2,1,3,0]
    print(even_numbers.find_even_numbers(digits))
    print(even_numbers.find_even_numbers_dict(digits))
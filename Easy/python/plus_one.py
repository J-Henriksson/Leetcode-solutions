from typing import List

class PlusOne():
    def plus_one(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        result = digits[index] + 1

        digits[index] = result

        while result >= 10:
            digits[index] = result % 10
            index -= 1
            if index < 0:
                digits.insert(0, 1)
                result = 0
            else:
                result = digits[index] + 1
                digits[index] = result
        return digits


if __name__ == "__main__":
    plus_one = PlusOne()

    test_1 = [1,2,3]
    test_2 = [9]
    test_3 = [9, 9, 9]

    print(plus_one.plus_one(test_1))
    print(plus_one.plus_one(test_2))
    print(plus_one.plus_one(test_3))



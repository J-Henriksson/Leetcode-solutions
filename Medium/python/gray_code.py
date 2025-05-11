from typing import List

class GrayCode(object):

    def gray_code(self, n: int) -> List[int]:
        start_list = [0, 1]
        for p in range(1, n):
            temp_list = list(reversed(start_list))
            for index in range(len(temp_list)):
                temp_list[index] += 2**p
            start_list += temp_list
        return start_list


if __name__ == "__main__":
    gray_coder = GrayCode()
    print(gray_coder.gray_code(3))
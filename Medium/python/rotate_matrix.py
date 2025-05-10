from typing import List

class RotateMatrix(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        #start by vertically flipping it. This is the same as just inverting the order of a list.
        for index in range(len(matrix) // 2):
            matrix[index], matrix[len(matrix) - 1 - index] = matrix[len(matrix) - 1 - index], matrix[index]

        #Transpose the new matrix. First elements in every row will become the elements in the first row and so on...
        for n in range(len(matrix)):
            for p in range(n, len(matrix)):
                matrix[n][p], matrix[p][n] = matrix[p][n], matrix[n][p]




if __name__ == "__main__":
    rotateor = RotateMatrix()
    test_list = [[1, 2], [3, 4]]

    rotateor.rotate(test_list)
    print(test_list)
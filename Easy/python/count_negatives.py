from typing import List

class CountNegatives():
    
    def count_negatives(self, grid: List[List[int]]) -> int:
        
        """Basically since the matrix is sorted in descending order both horizontally and vertically
        we can use this to effectively traverse the matrix and determine the number of elements in
        each column and row that are negative.
        Depending on if the number we encounter when we traverse a row is negative or positive we can
        determine the following:
        If it's negative we know that:
        * All of the elements in the same column below it are negative.
        * All elements in the same row to the right are negative, which also means that all elements in 
        the same column as these elements below them are also negative.
        When we encounter a negative element we move to the LEFT.
        
        If it's positive we know that:
        * All of the elements in the same column above it are positive.
        * All elements in the same row to the left are positive.
        When we encounter a positive element we move DOWN.
        
        We stop when we either are on a positive number and can't go down more OR when we're at a negative number and can't go to the left more.
        i.e when our next move according to the formula puts us out of bounds of the matrix.
        """ 
        
        count = 0
        x,y = len(grid[0]) - 1,0
        
        while y < len(grid):
            current = grid[y][x]
    
            if current >= 0:
                count += len(grid[y]) - 1 - x
                y += 1
            elif x == 0:
                count += len(grid[y])
                y += 1
            else:
                x -= 1
        return count
    
if __name__ == "__main__":
    counter = CountNegatives()
    grid_1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    grid_2 = [[5,4,-1,-2]]
    print(counter.count_negatives(grid_1))
    print(counter.count_negatives(grid_2))
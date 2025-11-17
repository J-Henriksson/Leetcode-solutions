from typing import List

class NumIslands():
    
    def num_islands(self, grid: List[List[str]]) -> int:
        land_tiles = set()
        islands = 0
        """Basically we just wanna go through each cell, if cell is in landlist
        skip it. Else perform dfs and append each 1 to landlist."""
        
        for i in range(len(grid)):
            for r in range(len(grid[i])):
                if grid[i][r] == "1" and (i,r) not in land_tiles:
                    islands += 1
                    land_tiles.add((i, r))
                    self.dfs(grid, (i,r), land_tiles)                
        return islands
    
    def dfs(self, grid: List[List[str]], tile: tuple[int, int], land_tiles: List[tuple[int, int]]):
        x, y = tile[0], tile[1]
        adjacent = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for position in adjacent:
            if position[0] >= 0 and position[0] < len(grid):
                if position[1] >= 0 and position[1] < len(grid[position[0]]):
                    if grid[position[0]][position[1]] == "1" and (position[0], position[1]) not in land_tiles:
                        land_tiles.add(position)
                        self.dfs(grid, position, land_tiles)
                        
if __name__ == "__main__":
    islands = NumIslands()
    grid_1 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ] 
    grid_2 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    
    print(islands.num_islands(grid_1))
    print(islands.num_islands(grid_2))
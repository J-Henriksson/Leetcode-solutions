from typing import List
class PacificAtlanticFlow():
    directions = [(-1, 0), (1,0), (0, -1), (0,1)]

    
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pacific
        pacific_list = set()
        for i in range(len(heights[0])):
            self.dfs_water_flow(heights, (0,i), pacific_list) 
        for i in range(len(heights)):
            self.dfs_water_flow(heights, (i,0), pacific_list) 
        #atlantic
        atlantic_list = set()
        for i in range(len(heights[0])):
            self.dfs_water_flow(heights, (len(heights) - 1,i), atlantic_list) 
        for i in range(len(heights)):
            self.dfs_water_flow(heights, (i,len(heights[0]) - 1), atlantic_list) 
            
        return list(pacific_list & atlantic_list)
            
    def dfs_water_flow(self, heights: List[List[int]], coordinate: tuple[int, int], flow_list):
        if coordinate not in flow_list: flow_list.add(coordinate)
        for dx,dy in self.directions:
            x,y = coordinate[1] + dx, coordinate[0] + dy
            if (x >= 0 and x < len(heights[coordinate[0]])) and (y >= 0 and y < len(heights)):
                if heights[y][x] >= heights[coordinate[0]][coordinate[1]] and (y, x) not in flow_list:
                    self.dfs_water_flow(heights, (y, x), flow_list)

if __name__ == "__main__":
    flow = PacificAtlanticFlow()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    heights_2 = [[1]]
    
    print(flow.pacific_atlantic(heights))
    print(flow.pacific_atlantic(heights_2))

from typing import List
class ClimbStairsPrice():
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        #Basically we want to create an array that's continually filled with minimum cost to climb the stairs from an index starting from the top.
        #Each element will be the minimum of the two elements in front of
        min_cost = [cost[len(cost) - 1], cost[len(cost) - 2]]
        if len(cost) > 2:
            for i in range(len(cost) - 3, -1, -1):
                min_cost.append(cost[i] + min(min_cost[len(min_cost) - 1], min_cost[len(min_cost) - 2]))
        return min(min_cost[len(min_cost) - 1], min_cost[len(min_cost) - 2])
    

if __name__ == "__main__":
    min_stairs_cost = ClimbStairsPrice()
    stair_1 = [1, 2]
    stair_2 = [10,15,20]
    stair_3 = [1,100,1,1,1,100,1,1,100,1]
    
    print(min_stairs_cost.min_cost_climbing_stairs(stair_1))
    print(min_stairs_cost.min_cost_climbing_stairs(stair_2))
    print(min_stairs_cost.min_cost_climbing_stairs(stair_3))
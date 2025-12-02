from typing import List
from __future__ import annotations

class Node():
    def __init__(self, value: int, neighbors: List[Node]):
        self.value = value
        self.neighbors = neighbors

class DFS():
    
    def dfs(self, node: Node, visited: List[Node], goal: int) -> bool:
        if node.value == goal:
            return True
        visited.append(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, goal):
                    return True
                
    def dfs_iterative(self, node: Node, goal: int) -> bool:
        stack = []
        visited = []
        stack.append(node)
        while len(stack) != 0:
            current = stack.pop(0)
            if current.value == goal:
                return True
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.insert(0, neighbor)
                    visited.append(neighbor)
        return False
    
    def bfs(self, node: Node, goal: int) -> bool:
        stack = []
        visited = []
        stack.append(node)
        while len(stack) != 0:
            current = stack.pop(0)
            if current.value == goal:
                return True
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        return False
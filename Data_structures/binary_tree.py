from typing import List

class BinaryTreeNode():
    def __init__(self, value: int):
        self.left = None
        self.right = None
        self.val = value
    
class BinaryTree():
    def __init__(self, root: int):
        self.root = BinaryTreeNode(root)
    
    def insert(self, value: int):
        self.recursive_insert(self.root, value)
    def recursive_insert(self, node: BinaryTreeNode, value):
        if node == None:
            return BinaryTreeNode(value)
        if value > node.val:
            node.right = self.recursive_insert(node.right, value)
        elif value < node.val:
            node.left = self.recursive_insert(node.left, value)
        return node
    
    def list_to_tree(self, nodes: List[int]) -> BinaryTreeNode:
        for node in nodes:
            self.insert(node)
                                                                                
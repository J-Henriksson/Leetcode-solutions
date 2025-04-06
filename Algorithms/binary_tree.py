class BinaryTreeNode():
    def __init__(self, value: int):
        self.left_node = None
        self.right_node = None
        self.value = value
    
class BinaryTree():
    def __init__(self, root: BinaryTreeNode):
        self.root = root
    
    def insert(self, value: int):
        self.recursive_insert(self.root, value)
    def recursive_insert(self, node: BinaryTreeNode, value):
        if node == None:
            return BinaryTreeNode(value)
        if value > node.value:
            node.right_node = self.recursive_insert(node.right_node, value)
        elif value < node.value:
            node.left_node = self.recursive_insert(node.left_node, value)
        return node
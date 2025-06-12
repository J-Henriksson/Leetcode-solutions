from ...Data_structures.binary_tree import BinaryTreeNode, BinaryTree

class InvertTree():
    def invert_tree(self, root: BinaryTreeNode):
        if root != None:
            root_left = root.left_root
            root.left_root = self.invert_tree(root.right_root)
            root.right_root = self.invert_tree(root_left)
        return root
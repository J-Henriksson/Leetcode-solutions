from Data_structures.binary_tree import BinaryTreeNode

class HouseRobber3():
    def rob_tree(self, root: BinaryTreeNode) -> int:
        return max(self.dfs_sum(root))
    
    def dfs_sum(self, node: BinaryTreeNode):
        if node == None:
            return 0, 0
        rob_sum, skip_sum = 0, 0
        for child in (node.left, node.right):
            rob_child, skip_child = self.dfs_sum(child)
            rob_sum += skip_child
            skip_sum += max(rob_child, skip_child)
        return node.val + rob_sum, skip_sum
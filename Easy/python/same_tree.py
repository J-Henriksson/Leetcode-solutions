from Data_structures.binary_tree import BinaryTreeNode, BinaryTree

class SameTree():
    def is_same_tree(self, p: BinaryTreeNode, q: BinaryTreeNode) -> bool:
        return self.is_same_tree_recursive(p, q)
    
    def is_same_tree_recursive(self, p: BinaryTreeNode, q: BinaryTreeNode) -> bool:
        if p != None and q != None:
            if p.val != q.val:
                return False
            return self.is_same_tree_recursive(p.left, q.left) and self.is_same_tree_recursive(p.right, q.right)
        elif p == None and q == None:
            return True
        else:
            return False
        

if __name__ == "__main__":
    tree1 = BinaryTree(5)
    tree1.list_to_tree([6, 7, 3, 2])
    
    tree2 = BinaryTree(5) 
    tree2.list_to_tree([6, 7, 3, 2, 9])
    
    same = SameTree()
    print(same.is_same_tree(tree1.root, tree2.root))
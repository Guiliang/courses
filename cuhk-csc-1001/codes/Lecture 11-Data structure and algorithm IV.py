"""
======================================================
Lecture 11: Data Structure and Algorithm IV
Instructor: Guiliang Liu
School of Data Science
Topic: Tree, Binary Tree, DFS, BFS
======================================================
"""

# =====================================================
# Page 5~7: Definition of Tree and Node
# =====================================================

class TreeNode:
    """A general tree node with multiple children."""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        """Add a child node."""
        child.parent = self
        self.children.append(child)

    def is_leaf(self):
        """Check if the node is a leaf."""
        return len(self.children) == 0

    def get_depth(self):
        """Compute the depth of the node (distance to root)."""
        depth = 0
        current = self
        while current.parent:
            current = current.parent
            depth += 1
        return depth

    def display(self):
        """Recursively display tree structure."""
        indent = " " * self.get_depth() * 4
        prefix = indent + ("|-- " if self.parent else "")
        print(prefix + str(self.data))
        for child in self.children:
            child.display()


# =====================================================
# Page 10~14: Binary Tree Structure
# =====================================================

class BinaryTreeNode:
    """A node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"BinaryTreeNode({self.data})"


class BinaryTree:
    """Binary tree implementation."""
    def __init__(self, root_data=None):
        self.root = None
        if root_data is not None:
            self.root = BinaryTreeNode(root_data)

    def insert_left(self, current_node, data):
        """Insert a new node as the left child."""
        new_node = BinaryTreeNode(data)
        current_node.left = new_node
        new_node.parent = current_node
        return new_node

    def insert_right(self, current_node, data):
        """Insert a new node as the right child."""
        new_node = BinaryTreeNode(data)
        current_node.right = new_node
        new_node.parent = current_node
        return new_node

    def preorder(self, node):
        """Pre-order traversal (Root → Left → Right)."""
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        """In-order traversal (Left → Root → Right)."""
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        """Post-order traversal (Left → Right → Root)."""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


# =====================================================
# Page 15~18: Example - Expression Tree
# =====================================================

# Expression Example:  (A * (B + C))
#          *
#        /   \
#      A      +
#           /   \
#          B     C

def create_expression_tree():
    tree = BinaryTree('*')
    left = tree.insert_left(tree.root, 'A')
    right = tree.insert_right(tree.root, '+')
    tree.insert_left(right, 'B')
    tree.insert_right(right, 'C')
    return tree


# =====================================================
# Page 20~23: Depth-First Search (DFS)
# =====================================================

def dfs(node, target):
    """Perform depth-first search for a value in a binary tree."""
    if node is None:
        return None
    print(f"Visiting Node: {node.data}")
    if node.data == target:
        print(f"Found target: {target}")
        return node
    found = dfs(node.left, target)
    if found:
        return found
    return dfs(node.right, target)


# =====================================================
# Page 25~27: Breadth-First Search (BFS)
# =====================================================

from collections import deque

def bfs(root, target):
    """Perform breadth-first search for a value in a binary tree."""
    if root is None:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(f"Visiting Node: {node.data}")
        if node.data == target:
            print(f"Found target: {target}")
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


# =====================================================
# Page 29: Demonstration of Tree, DFS, and BFS
# =====================================================

if __name__ == "__main__":
    print("=== General Tree Example ===")
    root = TreeNode("CEO")
    head_sales = TreeNode("Head of Sales")
    head_hr = TreeNode("Head of HR")
    root.add_child(head_sales)
    root.add_child(head_hr)
    head_sales.add_child(TreeNode("Sales Executive 1"))
    head_sales.add_child(TreeNode("Sales Executive 2"))
    root.display()

    print("\n=== Binary Tree Example ===")
    exp_tree = create_expression_tree()
    print("In-order traversal of expression tree:")
    exp_tree.inorder(exp_tree.root)
    print("\nPre-order traversal:")
    exp_tree.preorder(exp_tree.root)
    print("\nPost-order traversal:")
    exp_tree.postorder(exp_tree.root)

    print("\n\n=== DFS Example ===")
    dfs(exp_tree.root, 'B')

    print("\n=== BFS Example ===")
    bfs(exp_tree.root, 'B')
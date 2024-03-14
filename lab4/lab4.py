class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root:
        # Swap left and right subtrees
        root.left, root.right = root.right, root.left
        # Recursively invert left and right subtrees
        invertTree(root.left)
        invertTree(root.right)
    return root

# Create a sample binary tree
def create_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

# Invert the tree
sample_tree = create_sample_tree()
inverted_tree = invertTree(sample_tree)

# Print the inverted tree (should be 1 -> 3 -> 2 -> 5 -> 4)
def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

print_tree(inverted_tree)

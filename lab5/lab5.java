class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def inorder_traversal(node, prev_val):
            if not node:
                return True

            # Check left subtree
            if not inorder_traversal(node.left, prev_val):
                return False

            # Check current node
            if node.val <= prev_val:
                return False
            prev_val = node.val

            # Check right subtree
            return inorder_traversal(node.right, prev_val)

        # Initialize with negative infinity as the previous value
        return inorder_traversal(root, float('-inf'))

# Example usage:
# Construct a sample BST
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Create an instance of Solution
solution = Solution()
print(solution.isValidBST(root))  # Output: True

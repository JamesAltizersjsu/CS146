class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class TreeInverter {
    public TreeNode invertTree(TreeNode root) {
        if (root != null) {
            // Swap left and right subtrees
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;

            // Recursively invert left and right subtrees
            invertTree(root.left);
            invertTree(root.right);
        }
        return root;
    }

    // Example usage
    public static void main(String[] args) {
        // Create a sample binary tree
        //       1
        //      / \
        //     2   8
        //    / \  /\
        //   3   4  5 6
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(3;
        root.left.right = new TreeNode(4);
        root.left.left = new TreeNode(5);
        root.left.right = new TreeNode(6);
        // Invert the tree
        TreeInverter inverter = new TreeInverter();
        TreeNode invertedRoot = inverter.invertTree(root);

        // Print the inverted tree (should be 1 -> 3 -> 2 -> 5 -> 4)
        printTree(invertedRoot);
    }

    private static void printTree(TreeNode root) {
        if (root != null) {
            System.out.println(root.val);
            printTree(root.left);
            printTree(root.right);
        }
    }
}

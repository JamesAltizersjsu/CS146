

Method Overview:
The isValidBST method checks whether a given binary tree is a valid binary search tree (BST).
It uses a helper method that recursively validates each subtree within the specified bounds.
Helper Method: Recursive Validation:
The helper method takes three parameters:
node: The current node being checked.
min_val: The minimum allowed value for nodes in the subtree.
max_val: The maximum allowed value for nodes in the subtree.
The initial call to the helper method starts with the root of the entire tree and negative infinity as the minimum bound and positive infinity as the maximum bound.

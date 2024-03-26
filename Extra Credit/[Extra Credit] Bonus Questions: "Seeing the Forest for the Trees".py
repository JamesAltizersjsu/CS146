class RBNode:
    def __init__(self, val):
        self.red = False  # Color: True for red, False for black
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

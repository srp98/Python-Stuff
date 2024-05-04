class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Invert Tree
def invert_tree(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)
    return node


# Tree traversal, printing tree
def print_tree(node):
    print(node.val)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

reversal_tree = invert_tree(root)
print('')
print_tree(root)
print()
print_tree(reversal_tree)

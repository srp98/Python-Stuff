class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invert_tree(node):
    """
    Function inverting the tree
    :param node: type TreeNode
    :return: node
    """
    if node is None:
        return None

    node.left, node.right = node.right, node.left

    invert_tree(node.left)
    invert_tree(node.right)

    return node


def print_tree(tree):
    """
    Prints the tree given
    :param tree: TreeNode object type
    :return: Tree
    """
    print(tree.val)
    if tree.left:
        print_tree(tree.left)
    if root.right:
        print_tree(tree.right)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)

print_tree(root)
invert_tree(root)
print_tree(root)

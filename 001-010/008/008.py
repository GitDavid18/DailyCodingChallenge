class node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def countUnivalSubTrees(node):
    if (node.left == None and node.right == None):
        return 1

    left_sub_trees = 0 if (
        node.left == node) else countUnivalSubTrees(node.left)
    right_sub_trees = 0 if (
        node.right == node) else countUnivalSubTrees(node.right)

    all_sub_trees = left_sub_trees + right_sub_trees

    if (node.left.value == node.right.value):
        all_sub_trees += 1

    return all_sub_trees


allOnes = node(1, node(1), node(1))
print(countUnivalSubTrees(allOnes))

root = node(0, node(1), node(0, node(1, node(1), node(1)), node(0)))
print(countUnivalSubTrees(root))

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialize(start_node):
    if (start_node == None):
        return 'None'

    return start_node.value + '(' + serialize(start_node.left) + ',' + serialize(start_node.right) + ')'


def deserialize(input):
    if input == 'None':
        return None

    value = input[:input.find('(')]
    sub_nodes = input[input.find('(') + 1: input.rfind(')')]
    middle = find_left_right_split(sub_nodes)
    left = deserialize(sub_nodes[:middle])
    right = deserialize(sub_nodes[middle + 1:])

    return Node(value, left, right)


def find_left_right_split(input):
    level = 0
    if (input.find('(') == -1):
        return input.find(',')
    for i in range(len(input)):
        if input[i] == '(':
            level += 1
        if input[i] == ')':
            level -= 1
            if (level == 0):
                return input[i:].find(',') + i

    # Test
    # Tree
    #             root
    #         left    right
    #      left.left


    # string root(left(left.left,None),right(None,None))
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
# print(deserialize(serialize(node)))

assert deserialize(serialize(node)).left.left.value == 'left.left'
print(deserialize(serialize(node)).left.left.value == 'left.left')

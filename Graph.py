

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = []


class Solution:

    def numIsland(self, root, parent):
        if not root:
            return 0
        numOfIsland = 0
        if parent == 0 and root.val == 1:
            numOfIsland += 1

        numOfIsland += sum([numIsland(child, root.val) for child in root.children])

        return numOfIsland

    def solve(self, root):
        return self.numIsland(root, 0)


def numIsland(root):
    if not root:
        return 0

    stack = [(root, 0)]  # Stack stores tuples of (node, parent_value)
    num_of_island = 0

    while stack:
        current_node, parent_value = stack.pop()

        # Check if the current node starts a new island
        if parent_value == 0 and current_node.val == 1:
            num_of_island += 1

        # Add children to the stack with the current node's value as the parent
        for child in current_node.children:
            stack.append((child, current_node.val))

    return num_of_island
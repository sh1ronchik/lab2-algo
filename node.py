class Node:
    def __init__(self, left=None, right=None):
        self.left_border, self.right_border = left, right
        self.left_child, self.right_child = None, None
        self.value = 0

    def copy_without_children(node):
        new_node = Node(node.left_border, node.right_border)
        new_node.value = node.value
        return new_node
    
    def copy_of_node(node, v):
        new_node = Node(node.left_border, node.right_border)
        new_node.value = node.value + v
        new_node.left_child = node.left_child
        new_node.right_child = node.right_child
        return new_node
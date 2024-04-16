class Node:
    
    def __init__(self, left=None, right=None):
        """
        Initializes a Node instance with the given left and right borders.

        :param left: The left border of the node.
        :param right: The right border of the node.
        """
        self.left_border, self.right_border = left, right
        self.left_child, self.right_child = None, None
        self.value = 0

    @staticmethod
    def copy_without_children(node):
        """
        Creates a new node with the same borders as the given node but without children.

        :param node: The node to copy.
        :return: A new node with the same borders as the given node.
        """
        new_node = Node(node.left_border, node.right_border)
        new_node.value = node.value
        return new_node

    @staticmethod
    def copy_of_node(node, v):
        """
        Creates a new node with the same borders as the given node and the same children,
        but with an updated value.

        :param node: The node to copy.
        :param v: The new value for the node.
        :return: A new node with the same borders and children as the given node, but with an updated value.
        """
        new_node = Node(node.left_border, node.right_border)
        new_node.value = node.value + v
        new_node.left_child = node.left_child
        new_node.right_child = node.right_child
        return new_node
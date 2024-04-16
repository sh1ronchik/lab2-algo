from node import Node

class Tree:

    def __init__(self) -> None:
        """
        Initializes an empty Tree instance.
        """
        self.root = None

    def create_tree(self, left, right):
        """
        Creates a new tree with the given left and right borders.

        This method recursively builds the tree, dividing the range into two halves
        until the range is small enough to be a leaf node.

        :param left: The left border of the tree.
        :param right: The right border of the tree.
        :return: The root node of the new tree.
        """
        node = Node(left, right)
        if left + 1 < right:
            mid = (right + left) // 2
            node.left_child = self.create_tree(left, mid)
            node.right_child = self.create_tree(mid, right)
        return node

    def change_tree(self, node, left, right, value):
        """
        Changes the value of the nodes within the given range. This method recursively traverses the tree, 
        updating the value of nodes.

        :param node: The current node.
        :param left: The left border of the range.
        :param right: The right border of the range.
        :param value: The value to add to the nodes within the range.
        :return: The modified node.
        """
        if left <= node.left_border and node.right_border <= right:
            return Node.copy_of_node(node, value)
        if right <= node.left_border or node.right_border <= left:
            return node
        new_node = Node.copy_without_children(node)
        new_node.left_child = self.change_tree(node.left_child, left, right, value)
        new_node.right_child = self.change_tree(node.right_child, left, right, value)
        return new_node

    def find(self, node, target):
        """
        Finds the value of the node that contains the target value. This method recursively traverses the tree, 
        checking if the target value falls within the current node's range. 

        :param node: The current node.
        :param target: The target value to find.
        :return: The value of the node that contains the target value.
        """
        if not node.right_child and not node.left_child:
            return node.value
        mid = (node.right_border + node.left_border) // 2
        if target < mid:
            return node.value + self.find(node.left_child, target)
        return node.value + self.find(node.right_child, target)
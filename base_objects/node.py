class Node:
    def __init__(self, left=None, right=None):
        self.left_border, self.right_border = left, right
        self.left_child, self.right_child = None, None
        self.value = 0

    def copy_without_children(self):
        new_node = self.__class__(self.left_border, self.right_border)
        new_node.value = self.value
        return new_node

    def copy_of_node(self, v):
        new_node = self.__class__(self.left_border, self.right_border)
        new_node.value = self.value + v
        new_node.left_child = self.left_child
        new_node.right_child = self.right_child
        return new_node
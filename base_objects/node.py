class Node:
    def __init__(self, left=None, right=None, value=0):
        self.left_border, self.right_border = left, right
        self.left_child, self.right_child = None, None
        self.value = value

    def copy_without_children(self):
        return self.__class__(self.left_border, self.right_border, self.value)

    def copy_of_node(self, v):
        return self.__class__(self.left_border, self.right_border, self.value + v, self.left_child, self.right_child)
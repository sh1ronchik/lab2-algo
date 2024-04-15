from node import Node

class Tree:
    def __init__(self) -> None:
        self.root = None

    def create_tree(self, left, right):
        node = Node(left, right)
        if left + 1 < right:
            mid = (right + left) // 2
            node.left_child = self.create_tree(left, mid)
            node.right_child = self.create_tree(mid, right)
        return node

    def change_tree(self, node, left, right, value):
        if left <= node.left_border and node.right_border <= right:
            return Node.copy_of_node(node, value)
        if right <= node.left_border or node.right_border <= left:
            return node
        new_node = Node.copy_without_children(node)
        new_node.left_child = self.change_tree(node.left_child, left, right, value)
        new_node.right_child = self.change_tree(node.right_child, left, right, value)
        return new_node

    def find(self, node, target):
        if not node.right_child and not node.left_child:
            return node.value
        mid = (node.right_border + node.left_border) // 2
        if target < mid:
            return node.value + self.find(node.left_child, target)
        return node.value + self.find(node.right_child, target)
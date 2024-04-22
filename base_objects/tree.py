from base_objects.node import Node

class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, left, right):
        if left + 1 >= right:
            return Node(left, right)
        mid = (right + left) // 2
        return Node(left, right, self.create_tree(left, mid), self.create_tree(mid, right))

    def change_tree(self, node, left, right, value):
        if left <= node.left_border <= right:
            return node.copy_of_node(value)
        if node.left_border > right or node.right_border < left:
            return node
        new_node = node.copy_without_children()
        new_node.left_child = self.change_tree(node.left_child, left, right, value)
        new_node.right_child = self.change_tree(node.right_child, left, right, value)
        return new_node

    def find(self, node, target):
        if not node.right_child and not node.left_child:
            return node.value
        mid = (node.right_border + node.left_border) // 2
        return node.value + (self.find(node.left_child, target) if target < mid else self.find(node.right_child, target))

    def bin_search(self, mass, target):
        if target < mass[0] or target > mass[-1]:
            return -1
        left, right = 0, len(mass) - 1
        while left < right:
            mid = (left + right) // 2
            if mass[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if mass[left] == target else -1
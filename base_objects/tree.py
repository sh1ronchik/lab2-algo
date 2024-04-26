from base_objects.node import Node

class Tree:
    def __init__(self):
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
            return node.copy_of_node(value)
        if right <= node.left_border or node.right_border <= left:
            return node
        new_node = node.copy_without_children()
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

    def bin_search(self, mass, target):
        if target < mass[0] or target > mass[-1]:
            return -1
        left, right = 0, len(mass)
        while right - left > 1:
            mid = (right + left) // 2
            if mass[mid] >= target:
                right = mid
            else:
                left = mid
        if mass[right] == target:
            return right
        return left
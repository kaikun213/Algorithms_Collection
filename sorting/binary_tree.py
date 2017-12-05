# Simple binary tree structure with limited functionality in python
# Operations in O(log n) = O(height) of the tree for balanced tree
# O(n) in worst case (e.g. insert sorted list, search last item)

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def root():
        return self.root

    def insert_node(self, element):
        self.internal_insert_node(self.root,element)

    def internal_insert_node(self,child,element):
        if self.root is None:
            self.root = Node(element)
        else:
            if child is None:
                child = Node(element)
            elif child.data <= element:
                child.right = self.internal_insert_node(child.right,element)
            elif child.data > element:
                child.left = self.internal_insert_node(child.left,element)
        return child

    # search returns None if not in tree
    def search(self, element):
        if self.root is None:
            return None
        else:
            internal_search(self.root, element)

    def internal_search(self, child, element):
        if child is None:
            return None
        elif child.data < element:
            self.internal_search(child.right,element)
        elif child.data > element:
            self.internal_search(child.left,element)
        # found element
        return child

    def PreOrder(self):
        self.internalPreOrder(self.root)

    def internalPreOrder(self, root):
        if root is not None:
            print(root.data)
            if root.left is not None:
                self.internalPreOrder(root.left)
            if root.right is not None:
                self.internalPreOrder(root.right)


tree = BinaryTree()
tree.insert_node(5)
tree.insert_node(2)
tree.insert_node(12)
tree.insert_node(10)
tree.PreOrder()

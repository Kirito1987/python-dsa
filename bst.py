"""
Binary Search Tree (BST) Implementation in Python
---------------------------------------------------
A BST is a tree where each node's left child contains only values less than
the node, and the right child contains only values greater. This property
makes search, insert, and delete very efficient on balanced trees.

Time Complexity (average case):
    - Insert:  O(log n)
    - Search:  O(log n)
    - Delete:  O(log n)
    - Worst case (unbalanced): O(n)
Space Complexity: O(n)
"""


class BSTNode:
    """Represents a single node in the Binary Search Tree."""

    def __init__(self, value):
        self.value = value
        self.left = None   # Left child (smaller values)
        self.right = None  # Right child (larger values)


class BinarySearchTree:
    """Binary Search Tree with insert, search, and traversal operations."""

    def __init__(self):
        self.root = None

    # ── Insert ────────────────────────────────────────────────────────────────

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Helper: recursively find the correct position and insert."""
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
        # If value == node.value, we ignore duplicates

    # ── Search ────────────────────────────────────────────────────────────────

    def search(self, value):
        """
        Search for a value in the BST.
        Returns True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper: recursively search left or right based on value."""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # ── Traversals ────────────────────────────────────────────────────────────

    def inorder(self):
        """
        In-order traversal: Left -> Root -> Right.
        Returns a sorted list of all values in the BST.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        """
        Pre-order traversal: Root -> Left -> Right.
        Useful for copying or serializing a tree.
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        """
        Post-order traversal: Left -> Right -> Root.
        Useful for deleting a tree or evaluating expressions.
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # ── Delete ────────────────────────────────────────────────────────────────

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Helper: handle three cases — no child, one child, two children."""
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: Leaf node (no children)
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: Two children — replace with in-order successor
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _find_min(self, node):
        """Find the leftmost (minimum) node in a subtree."""
        while node.left:
            node = node.left
        return node


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    bst = BinarySearchTree()

    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("In-order (sorted):", bst.inorder())    # [20, 30, 40, 50, 60, 70, 80]
    print("Pre-order:", bst.preorder())            # [50, 30, 20, 40, 70, 60, 80]
    print("Post-order:", bst.postorder())          # [20, 40, 30, 60, 80, 70, 50]

    print("Search 40:", bst.search(40))            # True
    print("Search 99:", bst.search(99))            # False

    bst.delete(30)
    print("After deleting 30:", bst.inorder())     # [20, 40, 50, 60, 70, 80]

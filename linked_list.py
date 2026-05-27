"""
Linked List Implementation in Python
-------------------------------------
A singly linked list supports dynamic data storage where each node
points to the next. Useful when frequent insertions/deletions are needed
and random access is not required.

Time Complexity:
    - Insert at head: O(1)
    - Insert at tail: O(n)
    - Search:         O(n)
    - Delete:         O(n)
Space Complexity: O(n)
"""


class Node:
    """Represents a single node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    """Singly Linked List with core operations."""

    def __init__(self):
        self.head = None  # Empty list starts with no head

    def insert_at_head(self, data):
        """Insert a new node at the beginning of the list. O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert a new node at the end of the list. O(n)"""
        new_node = Node(data)

        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target):
        """
        Search for a value in the list.
        Returns the node if found, None otherwise. O(n)
        """
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def delete(self, target):
        """
        Delete the first node containing the target value. O(n)
        Returns True if deleted, False if not found.
        """
        if self.head is None:
            return False

        # Special case: target is the head
        if self.head.data == target:
            self.head = self.head.next
            return True

        # Traverse and find the node just before the target
        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next  # Bypass the target node
                return True
            current = current.next

        return False  # Target not found

    def to_list(self):
        """Convert linked list to a Python list for easy viewing."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        """String representation of the linked list."""
        return " -> ".join(str(val) for val in self.to_list()) + " -> None"


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_tail(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    ll.insert_at_head(5)
    print("After inserts:", ll)          # 5 -> 10 -> 20 -> 30 -> None

    ll.delete(20)
    print("After deleting 20:", ll)      # 5 -> 10 -> 30 -> None

    found = ll.search(10)
    print("Search for 10:", found.data if found else "Not found")  # 10

    not_found = ll.search(99)
    print("Search for 99:", not_found.data if not_found else "Not found")  # Not found

"""
Stack and Queue Implementations in Python
------------------------------------------
Two fundamental abstract data types used throughout software engineering:

Stack  — Last In, First Out (LIFO): think undo history, call stacks
Queue  — First In, First Out (FIFO): think task scheduling, print queues

Both are implemented using Python classes with O(1) core operations.
"""


# ── Stack ─────────────────────────────────────────────────────────────────────

class Stack:
    """
    Stack (LIFO) — Last element pushed is the first one popped.

    Real-world uses:
        - Browser back/forward navigation
        - Undo/redo in text editors
        - Function call stack in programming languages
        - Balanced parentheses checking

    Time Complexity:
        - push:  O(1)
        - pop:   O(1)
        - peek:  O(1)
        - empty: O(1)
    """

    def __init__(self):
        self._items = []  # Internal list used as the stack

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item.
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

    def __str__(self):
        return f"Stack (top -> bottom): {list(reversed(self._items))}"


# ── Queue ─────────────────────────────────────────────────────────────────────

class Queue:
    """
    Queue (FIFO) — First element enqueued is the first one dequeued.

    Real-world uses:
        - Task/job scheduling (OS process queues)
        - Breadth-First Search (BFS) in graphs
        - Print spoolers
        - Message queues in distributed systems

    Time Complexity:
        - enqueue: O(1)
        - dequeue: O(1)  (uses collections.deque for efficiency)
        - peek:    O(1)
        - empty:   O(1)
    """

    def __init__(self):
        # collections.deque allows O(1) popleft (vs O(n) with a plain list)
        from collections import deque
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the front item.
        Raises IndexError if queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._items.popleft()

    def peek(self):
        """
        Return the front item without removing it.
        Raises IndexError if queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek at an empty queue")
        return self._items[0]

    def is_empty(self):
        """Return True if the queue has no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def __str__(self):
        return f"Queue (front -> back): {list(self._items)}"


# ── Bonus: Balanced Parentheses Checker (Stack use case) ──────────────────────

def is_balanced(expression):
    """
    Check if brackets in an expression are balanced using a Stack.
    This is a classic interview problem that demonstrates Stack's power.

    Examples:
        "([]{})"  -> True
        "([)]"    -> False
        "{[}"     -> False
    """
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.push(char)          # Push opening brackets
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching[char]:
                return False          # Mismatch or nothing to match
    return stack.is_empty()           # All brackets matched if stack is empty


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Stack demo
    print("=== Stack Demo ===")
    s = Stack()
    s.push("first")
    s.push("second")
    s.push("third")
    print(s)                          # Stack (top -> bottom): ['third', 'second', 'first']
    print("Peek:", s.peek())          # third
    print("Pop:", s.pop())            # third
    print("After pop:", s)            # Stack (top -> bottom): ['second', 'first']

    # Queue demo
    print("\n=== Queue Demo ===")
    q = Queue()
    q.enqueue("task_1")
    q.enqueue("task_2")
    q.enqueue("task_3")
    print(q)                          # Queue (front -> back): ['task_1', 'task_2', 'task_3']
    print("Peek:", q.peek())          # task_1
    print("Dequeue:", q.dequeue())    # task_1
    print("After dequeue:", q)        # Queue (front -> back): ['task_2', 'task_3']

    # Balanced parentheses demo
    print("\n=== Balanced Parentheses ===")
    tests = ["([]{})", "([)]", "{[}", "((()))"]
    for t in tests:
        print(f"  '{t}' -> {'balanced' if is_balanced(t) else 'NOT balanced'}")

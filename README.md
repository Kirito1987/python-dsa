# Python Data Structures & Algorithms Showcase

A collection of core data structures and algorithms implemented in Python from scratch. Each module is self-contained, well-commented, and includes a runnable demo.

Built to reinforce computer science fundamentals and demonstrate clean, readable Python code.

---

## 📁 Structure

```
dsa_showcase/
├── linked_list.py    # Singly Linked List
├── bst.py            # Binary Search Tree
├── sorting.py        # Merge Sort, Bubble Sort, Binary Search
├── stack_queue.py    # Stack, Queue, and a classic use case
├── patient_queue.py  # Patient Triage Priority Queue (Min-Heap)
└── README.md
```

---

## 📦 Modules

### `linked_list.py` — Singly Linked List
A dynamic data structure where each node holds a value and a pointer to the next node.

| Operation       | Time Complexity |
|----------------|----------------|
| Insert at head | O(1)           |
| Insert at tail | O(n)           |
| Search         | O(n)           |
| Delete         | O(n)           |

```python
from linked_list import LinkedList

ll = LinkedList()
ll.insert_at_tail(10)
ll.insert_at_tail(20)
ll.insert_at_head(5)
print(ll)        # 5 -> 10 -> 20 -> None
ll.delete(10)
print(ll)        # 5 -> 20 -> None
```

---

### `bst.py` — Binary Search Tree
A tree where each node's left subtree contains smaller values and the right subtree contains larger values. Supports insert, search, delete, and three traversal methods.

| Operation  | Average  | Worst Case |
|-----------|----------|------------|
| Insert    | O(log n) | O(n)       |
| Search    | O(log n) | O(n)       |
| Delete    | O(log n) | O(n)       |

```python
from bst import BinarySearchTree

bst = BinarySearchTree()
for val in [50, 30, 70, 20, 40]:
    bst.insert(val)

print(bst.inorder())     # [20, 30, 40, 50, 70] — always sorted
print(bst.search(40))    # True
```

---

### `sorting.py` — Sorting Algorithms & Binary Search
Implements and compares two sorting algorithms plus an efficient search.

| Algorithm     | Time Complexity | Space | Stable |
|--------------|----------------|-------|--------|
| Merge Sort   | O(n log n)     | O(n)  | ✅     |
| Bubble Sort  | O(n²)          | O(1)  | ✅     |
| Binary Search | O(log n)      | O(1)  | —      |

```python
from sorting import merge_sort, binary_search

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)                        # [3, 9, 10, 27, 38, 43, 82]
print(binary_search(sorted_arr, 27))     # 3 (index)
print(binary_search(sorted_arr, 99))     # -1 (not found)
```

---

### `stack_queue.py` — Stack & Queue
Two fundamental abstract data types, each with O(1) core operations.

**Stack (LIFO)** — Last In, First Out
- Use cases: undo/redo, browser history, call stack, expression parsing

**Queue (FIFO)** — First In, First Out
- Use cases: task scheduling, BFS traversal, message queues

Includes a bonus **balanced parentheses checker** as a real-world Stack application.

```python
from stack_queue import Stack, Queue, is_balanced

s = Stack()
s.push(1)
s.push(2)
print(s.pop())    # 2

q = Queue()
q.enqueue("job_1")
q.enqueue("job_2")
print(q.dequeue())    # job_1

print(is_balanced("([{}])"))    # True
print(is_balanced("([)]"))      # False
```

---

### `patient_queue.py` — Patient Triage Priority Queue
A real-world simulation of a telehealth triage system built on a Min-Heap. Patients are prioritized by severity (1 = critical, 5 = routine), with arrival time as a tiebreaker. Demonstrates how priority queues power urgent, time-sensitive systems.

| Operation         | Time Complexity |
|------------------|----------------|
| Add patient       | O(log n)       |
| Next patient      | O(log n)       |
| Peek at next      | O(1)           |
| Check queue size  | O(1)           |

```python
from patient_queue import TriageQueue

queue = TriageQueue()
queue.add_patient("Maria Santos", 3, "Persistent headache")
queue.add_patient("James Okafor", 1, "Chest pain")   # Critical — goes first
queue.add_patient("Linda Chen",   4, "Sore throat")

queue.display_queue()

patient = queue.next_patient()
print(f"Now seeing: {patient.name}")   # James Okafor — severity 1
```

**Key features:**
- Min-heap ensures O(log n) insert and extract
- FIFO tiebreaker when two patients share the same severity
- Walk-in emergencies are re-prioritized instantly
- Session stats tracking (waiting, seen, total registered)

---

## 🚀 Running the Code

Each file can be run directly to see a demo:

```bash
python linked_list.py
python bst.py
python sorting.py
python stack_queue.py
python patient_queue.py
```

No external dependencies required — pure Python 3.

---

## 🧠 Concepts Covered

- **Linear structures**: Linked List, Stack, Queue
- **Tree structures**: Binary Search Tree with recursive algorithms
- **Heap structures**: Min-Heap based Priority Queue
- **Sorting**: Divide-and-conquer (Merge Sort) vs brute force (Bubble Sort)
- **Searching**: Binary Search on sorted arrays
- **Recursion**: Used throughout BST operations and Merge Sort
- **Real-world application**: Patient triage system modeled on telehealth workflows
- **Time & Space complexity analysis** documented on every function

---

## 👤 Author

[Kirito1987](https://github.com/Kirito1987)

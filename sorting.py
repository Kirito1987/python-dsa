"""
Sorting Algorithms & Binary Search in Python
----------------------------------------------
This module implements two classic algorithms:

1. Merge Sort  — A divide-and-conquer sorting algorithm
2. Binary Search — An efficient search on sorted arrays

These are fundamental CS concepts used in technical interviews and
real-world applications like database indexing and search systems.
"""


# ── Merge Sort ────────────────────────────────────────────────────────────────

def merge_sort(arr):
    """
    Merge Sort: Recursively splits the array in half, sorts each half,
    then merges them back together in sorted order.

    Time Complexity:  O(n log n) — guaranteed, even in worst case
    Space Complexity: O(n) — requires auxiliary space for merging

    Args:
        arr (list): The list to sort
    Returns:
        list: A new sorted list
    """
    # Base case: a list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Find the midpoint and split
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort left
    right_half = merge_sort(arr[mid:])  # Recursively sort right

    # Step 2: Merge the two sorted halves
    return _merge(left_half, right_half)


def _merge(left, right):
    """
    Helper: Merge two sorted lists into one sorted list.

    Uses two pointers to compare elements from each half,
    always picking the smaller one first.
    """
    merged = []
    i = j = 0

    # Compare elements from both halves and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements (one half may finish first)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# ── Binary Search ─────────────────────────────────────────────────────────────

def binary_search(arr, target):
    """
    Binary Search: Efficiently finds a target in a SORTED list by
    repeatedly halving the search space.

    Time Complexity:  O(log n) — much faster than linear search O(n)
    Space Complexity: O(1) — iterative approach, no extra space

    Args:
        arr (list): A sorted list to search through
        target: The value to find
    Returns:
        int: Index of the target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid          # Found it!
        elif arr[mid] < target:
            left = mid + 1      # Target is in the right half
        else:
            right = mid - 1     # Target is in the left half

    return -1  # Target not found


# ── Bubble Sort (Bonus — for comparison) ──────────────────────────────────────

def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly steps through the list, compares adjacent
    elements and swaps them if they're in the wrong order.

    Time Complexity:  O(n^2) — inefficient for large datasets
    Space Complexity: O(1) — sorts in place
    Included here to contrast with merge sort's efficiency.
    """
    arr = arr[:]  # Work on a copy to avoid mutating the input
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        # Early exit if no swaps occurred — already sorted
        if not swapped:
            break

    return arr


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    unsorted = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:        ", unsorted)

    ms_result = merge_sort(unsorted)
    print("After merge sort:      ", ms_result)   # [3, 9, 10, 27, 38, 43, 82]

    bs_result = bubble_sort(unsorted)
    print("After bubble sort:     ", bs_result)   # [3, 9, 10, 27, 38, 43, 82]

    # Binary search requires a sorted array
    sorted_arr = ms_result
    idx = binary_search(sorted_arr, 27)
    print(f"\nBinary search for 27:   index {idx}")   # index 3

    idx = binary_search(sorted_arr, 99)
    print(f"Binary search for 99:   index {idx}")     # index -1 (not found)

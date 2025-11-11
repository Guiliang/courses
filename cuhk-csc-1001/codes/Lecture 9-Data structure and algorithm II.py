"""
Lecture 9: Data Structure and Algorithm II
Topic: Recursion, Stack and Queue
Prof. Tongxin Li – School of Data Science

All lecture code examples combined and numbered sequentially.
"""

# ===============================================================
# 1. Sum of a list using recursion (linear recursion)
# ===============================================================

def recursive_sum(lst):
    """Return sum of a list using recursion."""
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])


# ===============================================================
# 2. Power function using recursion (O(log n))
# ===============================================================

def power(x, n):
    """Compute x^n using logarithmic recursion."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    else:
        return x * power(x, n - 1)


# ===============================================================
# 3. Binary sum using multiple recursion
# ===============================================================

def binary_sum(lst, start=0, stop=None):
    """Compute the sum of list[lst[start:stop]] using multiple recursion."""
    if stop is None:
        stop = len(lst)
    if start >= stop:
        return 0
    elif stop - start == 1:
        return lst[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(lst, start, mid) + binary_sum(lst, mid, stop)


# ===============================================================
# 4. Print reversed list using recursion
# ===============================================================

def print_reverse(lst, index=0):
    """Print elements in reverse order using recursion."""
    if index == len(lst):
        return
    print_reverse(lst, index + 1)
    print(lst[index], end=" ")


# ===============================================================
# 5. Merge sort using recursion
# ===============================================================

def merge_sort(lst):
    """Sort a list using merge sort."""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ===============================================================
# 6. Stack class (LIFO)
# ===============================================================

class Stack:
    """Stack data structure (Last‑In First‑Out)."""

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def __repr__(self):
        return f"Stack({self._data})"


# ===============================================================
# 7. Reverse a list using stack
# ===============================================================

def reverse_list(lst):
    """Reverse a list using the Stack class."""
    s = Stack()
    for item in lst:
        s.push(item)
    result = []
    while not s.is_empty():
        result.append(s.pop())
    return result


# ===============================================================
# 8. Brackets match checking using stack
# ===============================================================

def is_matched(expr: str) -> bool:
    """Check whether all brackets are balanced."""
    opening = "({["
    closing = ")}]"
    mapping = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for symbol in expr:
        if symbol in opening:
            stack.push(symbol)
        elif symbol in closing:
            if stack.is_empty():
                return False
            if stack.pop() != mapping[symbol]:
                return False
    return stack.is_empty()


# ===============================================================
# 9. Matching HTML tags using stack
# ===============================================================

def is_matched_html(raw: str) -> bool:
    """Check for matched HTML tags."""
    stack = Stack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith("/"):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if stack.pop() != tag[1:]:
                return False
        j = raw.find("<", k + 1)
    return stack.is_empty()


# ===============================================================
# 10. Queue class (FIFO)
# ===============================================================

class Queue:
    """Queue data structure (First‑In First‑Out)."""

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.pop(0)

    def __repr__(self):
        return f"Queue({self._data})"


# ===============================================================
# 11. Simulate a web service using queue
# ===============================================================

import random
import time

def simulate_web_service(num_requests=5):
    """Simulate queue processing (first‑come, first‑served)."""
    q = Queue()

    # enqueue incoming requests
    for i in range(1, num_requests + 1):
        q.enqueue(f"Request {i}")
        print(f"Received {q._data[-1]}")

    # process requests
    while not q.is_empty():
        request = q.dequeue()
        duration = random.uniform(0.2, 0.8)
        print(f"Processing {request} for {duration:.2f}s...")
        time.sleep(0.1)
    print("All requests processed.\n")


# ===============================================================
# 12. Stack vs Queue demonstration
# ===============================================================

def demonstrate_structures():
    s = Stack()
    q = Queue()
    for i in range(3):
        s.push(i)
        q.enqueue(i)
    print("Stack (LIFO) pop order :", [s.pop() for _ in range(3)])
    print("Queue (FIFO) dequeue order:", [q.dequeue() for _ in range(3)])


# ===============================================================
# 13. Driver demonstration
# ===============================================================

def main():
    print("\nRecursive sum:", recursive_sum([1, 2, 3, 4, 5]))
    print("\nPower (2, 10):", power(2, 10))
    print("\nBinary sum:", binary_sum([1, 2, 3, 4, 5, 6, 7, 8]))

    print("\nReverse printing recursively:")
    print_reverse([1, 2, 3])
    print("\n")

    print("\nMerge sort:", merge_sort([5, 2, 9, 1, 3, 7]))

    print("\nStack example:")
    s = Stack()
    for x in [1, 2, 3]:
        s.push(x)
    print("Stack after push:", s)
    print("Pop:", s.pop())

    print("\nReverse list using stack:", reverse_list([1, 2, 3, 4]))

    print("\nBracket check:")
    print("({[]}) →", is_matched("({[]})"))
    print("{(][])} →", is_matched("{(][])}"))

    print("\nHTML tag check:")
    html = "<html><body><h1>Hello</h1></body></html>"
    print("HTML matched?", is_matched_html(html))

    print("\nQueue simulation:")
    simulate_web_service(3)

    print("\nStack vs Queue order:")
    demonstrate_structures()


# ===============================================================
# 14. Entry Point
# ===============================================================

if __name__ == "__main__":
    main()
"""
Lecture 10 - Data Structure and Algorithm III
Topic: Linked Lists, Stacks, Queues, and Sorting Algorithms
Instructor: Guiliang Liu
School of Data Science
"""

# ==========================================================
# Singly Linked List
# ==========================================================

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly linked list implementation."""
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        """Insert a new node at the head."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        """Insert a new node at the tail."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def remove_head(self):
        """Remove the head node."""
        if self.head:
            self.head = self.head.next

    def traverse(self):
        """Traverse and print the linked list."""
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def find_middle(self):
        """Find the middle node using the slow-fast pointer technique."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def reverse(self):
        """Reverse the linked list iteratively."""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def has_cycle(self):
        """Detect if a linked list has a cycle using Floyd’s algorithm."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# ==========================================================
# Stack and Queue Using Linked List
# ==========================================================

class Stack:
    """Stack implemented with a singly linked list (LIFO)."""
    def __init__(self):
        self.list = SinglyLinkedList()

    def push(self, data):
        self.list.insert_head(data)

    def pop(self):
        if self.list.head:
            value = self.list.head.data
            self.list.remove_head()
            return value
        return None

    def peek(self):
        return self.list.head.data if self.list.head else None

    def is_empty(self):
        return self.list.head is None


class Queue:
    """Queue implemented with a singly linked list (FIFO)."""
    def __init__(self):
        self.list = SinglyLinkedList()

    def enqueue(self, data):
        self.list.insert_tail(data)

    def dequeue(self):
        if self.list.head:
            value = self.list.head.data
            self.list.remove_head()
            return value
        return None

    def is_empty(self):
        return self.list.head is None


# ==========================================================
# Doubly Linked List
# ==========================================================

class DoublyNode:
    """Node for a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly linked list with head and tail sentinels."""
    def __init__(self):
        self.head = DoublyNode(None)  # header sentinel
        self.tail = DoublyNode(None)  # trailer sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_between(self, data, predecessor, successor):
        """Insert a node between two others."""
        new_node = DoublyNode(data)
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node

    def insert_head(self, data):
        self.insert_between(data, self.head, self.head.next)

    def insert_tail(self, data):
        self.insert_between(data, self.tail.prev, self.tail)

    def delete_node(self, node):
        """Delete a non-sentinel node."""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        data = node.data
        node.prev = node.next = node.data = None
        return data


# ==========================================================
# Sorting Algorithms
# ==========================================================

def bubble_sort(arr):
    """Simple bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_linked_list(linked_list):
    """Bubble sort over a singly linked list by swapping values."""
    end = None
    while end != linked_list.head:
        cur = linked_list.head
        while cur.next != end:
            nxt = cur.next
            if cur.data > nxt.data:
                cur.data, nxt.data = nxt.data, cur.data
            cur = cur.next
        end = cur


def quick_sort(arr):
    """Quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


# ==========================================================
# Circularly Linked List & Josephus Problem
# ==========================================================

class CircularNode:
    """Node for circularly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularlyLinkedList:
    """Circular linked list implementation."""
    def __init__(self):
        self.tail = None

    def insert(self, data):
        new_node = CircularNode(data)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        """Remove head node."""
        if not self.tail:
            return None
        old_head = self.tail.next
        if self.tail == old_head:
            self.tail = None
        else:
            self.tail.next = old_head.next
        return old_head.data


def josephus_problem(n, k):
    """Solve the Josephus Problem using a circularly linked list."""
    circle = CircularlyLinkedList()
    for i in range(1, n + 1):
        circle.insert(i)

    cur = circle.tail
    while cur != cur.next:
        for _ in range(k - 1):
            cur = cur.next
        print(f"Eliminated: {cur.next.data}")
        circle.remove()
    return cur.data


# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.insert_tail(i)
    print("Original list:")
    ll.traverse()

    ll.reverse()
    print("Reversed list:")
    ll.traverse()

    print("Middle element:", ll.find_middle())

    print("Bubble sort example:", bubble_sort([4, 2, 7, 1, 3]))
    print("Quick sort example:", quick_sort([4, 2, 7, 1, 3]))
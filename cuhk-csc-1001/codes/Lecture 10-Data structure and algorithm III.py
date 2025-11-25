"""
======================================================
Lecture 10: Data Structure and Algorithm III
Instructor: Guiliang Liu
School of Data Science
Topic: Linked List & Sorting Algorithms
======================================================
"""

# =====================================================
# Page 10~11: Creating a Singly Linked List
# =====================================================

class Node:
    """Node class for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Basic singly linked list"""
    def __init__(self):
        self.head = None

    # =================================================
    # Page 12: Insert at the Head
    # =================================================
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # =================================================
    # Page 13: Insert at the Tail
    # =================================================
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # =================================================
    # Page 14: Remove from the Head
    # =================================================
    def remove_head(self):
        if self.head:
            self.head = self.head.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# =====================================================
# Page 21: Practice - Implement Stack (LIFO)
# =====================================================

class Stack:
    """Stack using singly linked list"""
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


# =====================================================
# Page 22: Practice - Implement Queue (FIFO)
# =====================================================

class Queue:
    """Queue using singly linked list"""
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


# =====================================================
# Page 24: Find the Middle Node
# =====================================================

def find_middle(linked_list):
    slow = fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None


# =====================================================
# Page 25~27: Reverse a Linked List
# =====================================================

def reverse(linked_list):
    prev = None
    curr = linked_list.head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    linked_list.head = prev


def reverse_recursive(node):
    """Reverse using recursion"""
    if node is None or node.next is None:
        return node
    rest = reverse_recursive(node.next)
    node.next.next = node
    node.next = None
    return rest


# =====================================================
# Page 30: Detect Cycle (Floyd’s Algorithm)
# =====================================================

def has_cycle(linked_list):
    slow = fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# =====================================================
# Page 33: Circularly Linked List
# =====================================================

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularlyLinkedList:
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
        """Remove head node"""
        if not self.tail:
            return None
        old_head = self.tail.next
        if self.tail == old_head:  # only one node
            self.tail = None
        else:
            self.tail.next = old_head.next
        return old_head.data


# =====================================================
# Page 37: The Josephus Problem
# =====================================================

def josephus_problem(n, k):
    circle = CircularlyLinkedList()
    for i in range(1, n + 1):
        circle.insert(i)

    current = circle.tail
    while current != current.next:
        for _ in range(k - 1):
            current = current.next
        print(f"Eliminated: {current.next.data}")
        circle.remove()
    return current.data


# =====================================================
# Page 38~41: Doubly Linked List
# =====================================================

class DoublyNode:
    """Node for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly linked list with head/tail sentinels"""
    def __init__(self):
        self.head = DoublyNode(None)  # header sentinel
        self.tail = DoublyNode(None)  # trailer sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_between(self, data, predecessor, successor):
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
        if node is self.head or node is self.tail:
            return None
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        data = node.data
        node.prev = node.next = node.data = None
        return data


# =====================================================
# Page 42: Optional - Bubble Sort
# =====================================================

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_linked_list(linked_list):
    end = None
    while end != linked_list.head:
        current = linked_list.head
        while current.next != end:
            nxt = current.next
            if current.data > nxt.data:
                current.data, nxt.data = nxt.data, current.data
            current = current.next
        end = current


# =====================================================
# Page 44~46: Quick Sort
# =====================================================

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


# =====================================================
# Test Section (for classroom use)
# =====================================================

if __name__ == "__main__":
    print("=== Singly Linked List Demo ===")
    sll = SinglyLinkedList()
    for x in [10, 20, 30]:
        sll.insert_tail(x)
    sll.traverse()
    print("Middle:", find_middle(sll))

    print("\n=== Reverse Linked List ===")
    reverse(sll)
    sll.traverse()

    print("\n=== Doubly Linked List Demo ===")
    dll = DoublyLinkedList()
    for x in ['A', 'B', 'C']:
        dll.insert_tail(x)
    cur = dll.head.next
    while cur != dll.tail:
        print(cur.data, end=" <-> ")
        cur = cur.next
    print("None")

    print("\n=== Sorting Examples ===")
    print("Bubble sort:", bubble_sort([4, 2, 7, 1, 3]))
    print("Quick sort:", quick_sort([4, 2, 7, 1, 3]))
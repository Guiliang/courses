"""
Lecture 8: Data Structure and Algorithm I
Prof. Guiliang Liu – School of Data Science

All code examples combined and numbered sequentially.
"""


# ------------------------------------------------------------
# 1. Finding the smallest number in a list
# ------------------------------------------------------------

def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest


# ------------------------------------------------------------
# 2. Factorial function (recursive)
# ------------------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)


# ------------------------------------------------------------
# 3. Recursive trace for factorial
# ------------------------------------------------------------

def trace_factorial(n, depth=0):
    indent = " " * depth
    print(f"{indent}factorial({n}) called")
    if n == 0:
        print(f"{indent}return 1")
        return 1
    else:
        result = n * trace_factorial(n - 1, depth + 2)
        print(f"{indent}return {result}")
        return result


# ------------------------------------------------------------
# 4. Drawing an English ruler (recursive)
# ------------------------------------------------------------

def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length and optional label."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """Draw the interval between major ticks."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches and major tick length."""
    draw_line(major_length, '0')
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


# ------------------------------------------------------------
# 5. Sequential search
# ------------------------------------------------------------

def sequential_search(data, target):
    """Return True if target is found, False otherwise."""
    for item in data:
        if item == target:
            return True
    return False


# ------------------------------------------------------------
# 6. Binary search (recursive)
# ------------------------------------------------------------

def binary_search(data, target, low, high):
    """Return True if target is found in sorted list data."""
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


# ------------------------------------------------------------
# 7. Counting primitive operations example
# ------------------------------------------------------------

def sum_list(lst):
    """Example for counting primitive operations."""
    total = 0  # 1 operation
    for item in lst:  # n iterations
        total += item  # n additions
    return total  # 1 return


# ------------------------------------------------------------
# 8. Experimental runtime measurement
# ------------------------------------------------------------

def test_function(n):
    """Simple test function to measure runtime complexity."""
    s = 0
    for i in range(n):
        s += i
    return s


def measure_runtime():
    """Empirical runtime experiment using time module."""
    import time
    sizes = [10 ** k for k in range(1, 6)]
    times = []

    for n in sizes:
        start = time.time()
        test_function(n)
        end = time.time()
        times.append(end - start)
        print(f"n={n}, time={end - start:.6f} seconds")

    return sizes, times


# ------------------------------------------------------------
# 10. Master demonstration function
# ------------------------------------------------------------

def main():
    print("\nFinding the Smallest Number")
    numbers = [5, 3, 7, 1, 9]
    print("Smallest number:", find_smallest(numbers))

    print("\nFactorial (Recursive)")
    print("Factorial of 5:", factorial(5))

    print("\nRecursive Trace for Factorial")
    trace_factorial(4)

    print("\nEnglish Ruler Demo")
    draw_ruler(2, 4)

    print("\nSequential Search")
    data = [5, 2, 8, 1, 3]
    print("Target 8 found?", sequential_search(data, 8))

    print("\nBinary Search")
    sorted_data = [1, 3, 5, 7, 9, 11, 13]
    print("Target 7 found?", binary_search(sorted_data, 7, 0, len(sorted_data) - 1))

    print("\nCounting Primitive Operations Example")
    print("Sum of [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))

    print("\nExperimental Runtime Measurement")
    sizes, times = measure_runtime()


if __name__ == "__main__":
    main()

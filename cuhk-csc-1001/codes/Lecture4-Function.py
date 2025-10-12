"""
==========================================================
Lecture 4 - Function, String, and File Operations in Python
Author: Guiliang Liu
==========================================================

This file consolidates all example codes, exercises, and
concept demonstrations from 'Lecture 4_Function_clean.pdf'.
Each section demonstrates a concept in Python programming.

Content Overview:
-----------------
1. Function Basics Example (Rectangle area)
2. Practice: Salary computation with overtime
3. Practice: Personal Income Tax function
4. String Operations (indexing, slicing, methods)
5. File Operations (reading, writing, line counting)
==========================================================
"""

# ==========================================================
# 1. FUNCTION BASICS - AREA OF A RECTANGLE
# ==========================================================

def calculate_rectangle_area(length, width):
    """Return the area of a rectangle given its length and width."""
    return length * width


def demo_rectangle_areas():
    """Demonstrate using the rectangle area function."""
    print("=== Rectangle Area Calculation ===")
    area1 = calculate_rectangle_area(10, 5)
    print("Area of rectangle 1:", area1)

    area2 = calculate_rectangle_area(7, 3)
    print("Area of rectangle 2:", area2)

    area3 = calculate_rectangle_area(12, 8)
    print("Area of rectangle 3:", area3)
    print("")


# ==========================================================
# 2. PRACTICE 1: SALARY CALCULATION WITH OVERTIME
# ==========================================================

def calculate_salary(hours, rate):
    """
    Compute total salary based on working hours and rate.
    If hours worked exceed 40, extra hours receive 1.5x pay.
    """
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * rate * 1.5
    return salary


def demo_salary():
    """Demonstrate salary calculation with and without overtime."""
    print("=== Salary Calculation ===")
    normal = calculate_salary(38, 10)
    overtime = calculate_salary(45, 10)

    print("Normal (38h @ $10/h): $", normal)
    print("Overtime (45h @ $10/h): $", overtime)
    print("")


# ==========================================================
# 3. PRACTICE 2: PERSONAL INCOME TAX FUNCTION
# ==========================================================

def tax(salary):
    """Return tax amount for a given annual salary based on progressive rates."""
    if salary < 36000:
        return salary * 0.03
    elif salary < 144000:
        return 36000 * 0.03 + (salary - 36000) * 0.1
    elif salary < 300000:
        return 36000 * 0.03 + (144000 - 36000) * 0.1 + (salary - 144000) * 0.2
    elif salary < 420000:
        return (36000 * 0.03 + (144000 - 36000) * 0.1 +
                (300000 - 144000) * 0.2 + (salary - 300000) * 0.25)
    elif salary < 660000:
        return (36000 * 0.03 + (144000 - 36000) * 0.1 +
                (300000 - 144000) * 0.2 + (420000 - 300000) * 0.25 +
                (salary - 420000) * 0.3)
    elif salary < 960000:
        return (36000 * 0.03 + (144000 - 36000) * 0.1 +
                (300000 - 144000) * 0.2 + (420000 - 300000) * 0.25 +
                (660000 - 420000) * 0.3 + (salary - 660000) * 0.35)
    else:
        return (36000 * 0.03 + (144000 - 36000) * 0.1 +
                (300000 - 144000) * 0.2 + (420000 - 300000) * 0.25 +
                (660000 - 420000) * 0.3 + (960000 - 660000) * 0.35 +
                (salary - 960000) * 0.45)


def demo_taxes():
    """Demonstrate tax calculations at multiple income levels."""
    print("=== Tax Calculation ===")
    salaries = [30000, 100000, 500000, 2000000]
    for s in salaries:
        t = tax(s)
        after_tax = s - t
        print("Salary:", s, "Tax:", t, "After-tax income:", after_tax)
    print("")

# ==========================================================
# 4. STRING OPERATIONS DEMONSTRATIONS
# ==========================================================

def string_operations():
    """Demonstrate string indexing, slicing, and common string methods."""
    print("=== String Operations ===")

    text = "  Hello World!  "
    print("Original string:", text)

    # Indexing
    print("First character:", text[0])
    print("Seventh character:", text[6])

    # Looping with for
    print("Characters in string:")
    for ch in text:
        print(ch, end=" ")
    print("\n")

    # Slicing
    print("Slicing [0:5]:", text[0:5])
    print("Slicing [7:]:", text[7:])
    print("Slicing [:5]:", text[:5])

    # "in" keyword
    if "World" in text:
        print("'World' found in text!")

    # String methods
    print("Lowercase:", text.lower())
    print("Uppercase:", text.upper())
    print("Find 'World':", text.find("World"))
    print("Replace 'World' -> 'Python':", text.replace("World", "Python"))
    print("Strip whitespace:", text.strip())
    print("Strip whitespace on the left:", text.lstrip())
    print("Strip whitespace on the right:", text.rstrip())
    print("Starts with 'Hello' after stripping:", text.strip().startswith("Hello"))
    print("")


def count_letter_a():
    """Count occurrences of 'a' in a string using a for loop."""
    print("=== Counting 'a's in a string ===")
    text = "banana"
    count = 0
    for ch in text:
        if ch == 'a':
            count = count + 1
    print("Number of 'a' in", repr(text), ":", count)
    print("")


def while_loop_string():
    """Loop through a string using while and len()."""
    print("=== While-loop iteration over string ===")
    s = "Python"
    i = 0
    while i < len(s):
        print(s[i])
        i = i + 1
    print("")


# ==========================================================
# 5. FILE OPERATIONS
# ==========================================================

def count_lines(filename):
    """Count how many lines are in a text file."""
    print("=== Count Lines in File ===")
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count = line_count + 1
        print("'" + filename + "' has", line_count, "lines.\n")
        return line_count
    except FileNotFoundError:
        print("File not found:", filename, "\n")
        return 0


def search_in_file(filename, keyword):
    """Print lines containing a specific keyword."""
    print("=== Searching for", repr(keyword), "in", filename, "===")
    try:
        with open(filename, 'r') as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError:
        print("File not found:", filename)
    print("")


def write_lowercase_file(input_file, output_file):
    """Read input file, convert to lowercase, and write to new file."""
    print("=== Writing Lowercase File ===")
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(line.lower())
        print("Lowercase content written to", repr(output_file))
        print("")
    except FileNotFoundError:
        print("File not found:", input_file, "- cannot process.")
        print("")


# ==========================================================
# MAIN EXECUTION - Run Demos
# ==========================================================

if __name__ == "__main__":
    # 1. Function Basics
    demo_rectangle_areas()

    # 2. Salary Calculation
    demo_salary()

    # 3. Tax Function
    demo_taxes()

    # 4. Strings
    string_operations()
    count_letter_a()
    while_loop_string()

    # 5. File Handling (requires existing text files)
    # You can uncomment these to test with your own files
    count_lines("example.txt")
    search_in_file("example.txt", "Python")
    write_lowercase_file("example.txt", "output.txt")

    print("=== End of Lecture 4 Demonstrations ===")
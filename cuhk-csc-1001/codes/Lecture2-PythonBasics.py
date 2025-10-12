"""
==========================================================
Lecture 2: Python Basics
Instructor: Prof. Guiliang Liu
==========================================================

This file demonstrates all important code examples from the lecture:
 1. Basic syntax and print
 2. Variables, constants, and assignment
 3. Numeric expressions and operator precedence
 4. Data types and type conversion
 5. User input and BMI calculation
 6. String operations and concatenation
 7. Using eval() for expression evaluation

All examples follow the Python 3 standard.
==========================================================
"""

# ==========================================================
# 1. HELLO WORLD & BASIC SYNTAX
# ==========================================================

# The simplest Python program:
print("Hello, world!")  # Output a message to the screen

# You can also exit Python by typing:
# exit()

# ==========================================================
# 2. USING PYTHON AS A CALCULATOR
# ==========================================================

# Python can directly do arithmetic operations interactively:
print("2 + 3 =", 2 + 3)
print("10 * 5 =", 10 * 5)
print("50 / 4 =", 50 / 4)
print("2 ** 3 =", 2 ** 3)   # Exponentiation
print("17 // 3 =", 17 // 3) # Floor division
print("17 % 3 =", 17 % 3)   # Remainder

# ==========================================================
# 3. VARIABLES AND ASSIGNMENT STATEMENTS
# ==========================================================

# Variables hold values in memory
x = 10
y = 5
print("x =", x, "y =", y)

# Example: assignment with an expression
x = 100 - 10 + x * 3 - x / 10
print("New x =", x)

# ==========================================================
# 4. CASCADED ASSIGNMENT & SIMULTANEOUS ASSIGNMENT
# ==========================================================

# Cascaded assignment: multiple variables assigned same value
a = b = c = 0
print("a =", a, "b =", b, "c =", c)

# Simultaneous assignment: swap variables easily
m = 3
n = 5
m, n = n, m  # swap values
print("After swapping:", "m =", m, "n =", n)

# ----------------------------------------------------------
# PRACTICE: Exchange the values of two variables without using simultaneous assignment
# ----------------------------------------------------------
p = 7
q = 9
print("Before swap:", "p =", p, "q =", q)

# Use a temporary variable
temp = p
p = q
q = temp
print("After swap:", "p =", p, "q =", q)

# ==========================================================
# 5. OPERATOR PRECEDENCE & NUMERIC EXPRESSIONS
# ==========================================================

# Operator precedence: (), **, *, /, //, %, +, -
result = 1 + 2 ** 3 / 4 * 5
print("Result of 1 + 2 ** 3 / 4 * 5 =", result)

# Using parentheses for clarity
result2 = 1 + ((2 ** 3) / 4) * 5
print("Result with parentheses =", result2)

# Integer division example
print("17 // 5 =", 17 // 5)  # floor division
print("Float division 17 / 5 =", 17 / 5)  # produces float

# Augmented assignment: shorthand for updating variable values
z = 10
z = z + 5  # same as z += 5
print("z after z = z + 5:", z)
z += 10
print("z after z += 10:", z)

# ==========================================================
# 6. DATA TYPES & TYPE CONVERSIONS
# ==========================================================

num1 = 10          # integer
num2 = 3.5         # float
text = "Python"    # string

print("num1 is", type(num1))
print("num2 is", type(num2))
print("text is", type(text))

# Type can change dynamically
value = 5
print("Before:", value, "type:", type(value))
value = "Five"
print("After:", value, "type:", type(value))

# Explicit type conversion
integer_part = int(3.9)
float_part = float(10)
print("Integer part of 3.9:", integer_part)
print("Float version of 10:", float_part)

# Converting strings into numbers
s_num = "25"
n = int(s_num)
print("Converted string '25' to int:", n, "plus 5 equals", n + 5)

# Converting numbers into string
num = 42
s = str(num)
print("Converted number 42 to string ->", s + ' is now a string')

# ==========================================================
# 7. USER INPUT
# ==========================================================

# input() always returns a string
# We must convert it to int or float for calculations

# Example 1: Read user’s name
# name = input("Enter your name: ")
# print("Hello,", name)

# ==========================================================
# 8. PRACTICE – BMI CALCULATOR
# ==========================================================

# BMI = weight (kg) / (height (m) ** 2)

# Get user input and convert to float
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# print("Your BMI is:", bmi)

# Example with sample data:
weight = 70.0
height = 1.75
bmi = weight / (height ** 2)
print("Sample BMI test with weight =", weight, "height =", height, "BMI =", bmi)

# ==========================================================
# 9. STRING OPERATIONS
# ==========================================================

# String concatenation with +
greeting = "Hello"
subject = "Python"
combined = greeting + " " + subject
print(combined)

# String repetition with *
laugh = "Ha" * 3
print("Using * to repeat string:", laugh)

# ==========================================================
# 10. PRACTICE – FRIENDS MESSAGES
# ==========================================================

# Write a program to prompt user for two friends’ names and display a sentence.
# friend1 = input("Enter your first friend’s name: ")
# friend2 = input("Enter your second friend’s name: ")
# print("I am the friend of " + friend1 + " and " + friend2 + ".")

# Example output with sample inputs:
friend1 = "Alice"
friend2 = "Bob"
print("I am the friend of " + friend1 + " and " + friend2 + ".")

# ==========================================================
# 11. COMMENTS
# ==========================================================

# Anything after a # is ignored by Python.
# Example below: the second line is a comment.
x = 5  # assign 5 to x
# print(x)  # this line is commented out

# ==========================================================
# 12. MORE ON PRINT()
# ==========================================================

# You can use commas to separate items in print()
a = 10
b = 20
print("a =", a, "and b =", b)

# print automatically adds a space between values.

# ==========================================================
# 13. THE eval() FUNCTION
# ==========================================================

# eval() evaluates a string as a Python expression
expr1 = "3 + 4 * 2"
result = eval(expr1)
print("Expression:", expr1, "evaluated to:", result)

# Example: evaluate user-supplied arithmetic (use with care!)
# expr2 = input("Enter a math expression (like 2 + 3 * 4): ")
# print("The result is:", eval(expr2))

# Demonstration:
expr2 = "2 + 3 * 4"
print("Example eval on", expr2, "=", eval(expr2))

# ==========================================================
# END OF LECTURE 2 EXAMPLES
# ==========================================================
print("=== End of Lecture 2 Demonstrations ===")
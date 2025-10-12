"""
==========================================================
Lecture 3: Flow Control
Instructor: Prof. Guiliang Liu
==========================================================

This file demonstrates:
 1. Conditional statements (if, if…else, if…elif…else)
 2. Nested flow control
 3. Logical operators
 4. Try / Except for error handling
 5. Repeated flow (loops)
 6. for-loops and while-loops
 7. Loop patterns: counting, summing, filtering, searching
==========================================================
"""

# ==========================================================
# 1. BOOLEAN EXPRESSIONS & COMPARISON OPERATORS
# ==========================================================

print("=== Comparison Operators & Boolean Expressions ===")
print("0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1 == 1 ?", 0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1 == 1)
x = 10
y = 20
print("x =", x, "y =", y)
print("x == y ?", x == y)
print("x != y ?", x != y)
print("x > y ?", x > y)
print("x < y ?", x < y)
print("x >= 10 ?", x >= 10)
print("y <= 15 ?", y <= 15)
print("")

# Lexicographic string comparison
print("Comparing strings …")
print("'Apple' < 'apple' ?", "Apple" < "apple")
print("'Banana' > 'Ant' ?", "Banana" > "Ant")
print("'cat' == 'Cat' ?", "cat" == "Cat")
print("")

# Boolean values
print("Boolean examples:")
print(bool(1), bool(0))  # True / False
print("Type of bool:", type(True))
print("")


# ==========================================================
# 2. SIMPLE IF STATEMENT
# ==========================================================

print("=== Basic if Statement Example ===")
x = 15
if x > 10:
    print("x is greater than 10")
print("Always printed after the if block")
print("")

# ----------------------------------------------------------
# PRACTICE: check if a student passes
# ----------------------------------------------------------
print("=== Practice: Grade Check ===")
grade = 57  # change this number to test
if grade >= 60:
    print("Passed")
if grade < 60:
    print("Failed")
print("")


# ==========================================================
# 3. IF … ELSE STATEMENT
# ==========================================================

print("=== if ... else Example ===")
grade = 85
if grade >= 60:
    print("You passed")
else:
    print("You failed")
print("")

# Nested if else
print("=== Nested if else Example ===")
score = 92
if score >= 90:
    print("Grade: A")
else:
    if score >= 80:
        print("Grade: B")
    else:
        print("Grade: below B")
print("")

# ==========================================================
# 4. IF … ELIF … ELSE (Multi-way decision)
# ==========================================================

print("=== Multi-way if...elif...else Example ===")
score = 76
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Fair")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
print("")


# ==========================================================
# 5. LOGICAL OPERATORS
# ==========================================================

print("=== Logical Operators ===")
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You are allowed to enter.")
else:
    print("Entry not permitted.")

# OR operator
temperature = 35
if temperature < 0 or temperature > 30:
    print("Temperature is extreme!")
else:
    print("Temperature is normal.")

# NOT operator
raining = False
if not raining:
    print("It is not raining.")
print("")


# ==========================================================
# 6. ERROR HANDLING: TRY / EXCEPT
# ==========================================================

print("=== try / except Example ===")
try:
    num = int("abc")  # this will cause ValueError
    print("Conversion successful:", num)
except:
    print("Error: invalid input detected.")
print("Program continues after handling error")
print("")

# Another example: check user input safely
# (simulate with test inputs)
print("=== try / except: Safe numeric input ===")
user_input = "xyz"
try:
    value = int(user_input)
    print("You entered:", value)
except:
    print("Invalid integer:", user_input)
print("")

# ==========================================================
# PRACTICE: Salary Calculation (with try/except)
# ==========================================================

print("=== Practice: Salary Calculation ===")
hours_input = "45"
rate_input = "10"
try:
    hours = float(hours_input)
    rate = float(rate_input)
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    print("Hours:", hours, "Rate:", rate, "Salary:", pay)
except:
    print("Error: invalid input for hours or rate")
print("")


# ==========================================================
# PRACTICE: Date + 1 day (leap years ignored)
# ==========================================================

print("=== Practice: Next Day Calculation (ignore leap year) ===")
month_input = 2
day_input = 28

try:
    month = int(month_input)
    day = int(day_input)
    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12 or day < 1 or day > days_in_month[month - 1]:
        print("Invalid date input!")
    else:
        day = day + 1
        if day > days_in_month[month - 1]:
            day = 1
            month = month + 1
            if month > 12:
                month = 1
        print("Next date -> Month:", month, "Day:", day)
except:
    print("Invalid data detected in month or day input.")
print("")


# ==========================================================
# 7. REPEATED FLOW (LOOPS)
# ==========================================================

print("=== Loops: for and while ===")

# While loop example
print("-- While loop demonstration --")
count = 0
while count < 5:
    print("Count =", count)
    count = count + 1
print("Loop finished\n")

# Infinite loop example (commented out)
# while True:
#     print("Infinite")

# For loop example
print("-- For loop demonstration --")
for i in [1, 2, 3, 4, 5]:
    print("i =", i)
print("End of for loop\n")


# ==========================================================
# 8. BREAK & CONTINUE EXAMPLES
# ==========================================================

print("=== Break and Continue Example ===")

for num in range(1, 6):
    if num == 3:
        print("Break at 3")
        break
    print("Current number:", num)
print("Loop finished after break\n")

for num in range(1, 6):
    if num == 3:
        print("Skip number 3 with continue")
        continue
    print("Current number:", num)
print("Loop finished after continue\n")


# ==========================================================
# 9. LOOP PATTERNS
# ==========================================================

# Sum Calculation
print("=== Loop Pattern: Sum Calculation ===")
numbers = [3, 7, 9, 12, 5]
total = 0
for num in numbers:
    total = total + num
print("Sum of", numbers, "=", total)
print("")

# Average Calculation
print("=== Loop Pattern: Average Calculation ===")
count = 0
sum_values = 0
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    sum_values = sum_values + num
    count = count + 1
print("Average =", sum_values / count)
print("")

# Finding the largest number
print("=== Finding the Largest Number ===")
numbers = [5, 12, 9, 33, 2]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number is:", largest)
print("")

# Finding the smallest number
print("=== Finding the Smallest Number ===")
numbers = [5, 12, 9, 33, 2]
smallest = None
for num in numbers:
    if smallest is None or num < smallest:
        smallest = num
print("Smallest number is:", smallest)
print("")

# Filtering in a loop
print("=== Filtering: Show numbers greater than 10 ===")
numbers = [5, 15, 3, 20, 8]
for num in numbers:
    if num > 10:
        print(num, "is greater than 10")
print("")

# Searching using a Boolean variable
print("=== Searching Example ===")
target = 7
numbers = [2, 4, 6, 8, 10]
found = False
for num in numbers:
    if num == target:
        found = True
if found:
    print("Found", target, "in the list")
else:
    print(target, "not found in the list")
print("")

# ==========================================================
# 10. "is" and "is not" Operator
# ==========================================================

print("=== 'is' and 'is not' Examples ===")
a = None
b = None
print("a is b ?", a is b)
print("a is not b ?", a is not b)
print("")

num1 = 5
num2 = 5
print("num1 is num2 ?", num1 is num2)
print("num1 == num2 ?", num1 == num2)
print("")


# ==========================================================
print("=== End of Lecture 3 Demonstrations ===")
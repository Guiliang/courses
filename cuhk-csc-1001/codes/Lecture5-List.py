"""
==========================================================
Lecture 5: List, Dictionary, and Tuple
Instructor: Prof. Benyou Wang
Reconstructed & Annotated by ChatGPT
==========================================================

This file demonstrates:

 1. Lists and basic list operations
 2. Loops with lists
 3. List slicing and methods
 4. Using range() and len()
 5. Building lists dynamically
 6. split() usage with strings
 7. Dictionaries and counting patterns
 8. Using get() method
 9. Looping through dictionaries
10. Tuples and sorting dictionary results

==========================================================
"""

# ==========================================================
# 1. Lists and collections
# ==========================================================

print("=== Lists and Collections ===")

x = [1, 2, 3, 4, 5]
print("List x:", x)

# A list can contain different types
mixed = [10, "apple", 3.14, [1, 2]]
print("Mixed list:", mixed)

# Lists can be empty
empty_list = []
print("Empty list:", empty_list)
print("")

# Not a collection example
a = 10
print("a =", a)
a = 20
print("After reassigning, a =", a)
print("")


# ==========================================================
# 2. Looking inside lists
# ==========================================================

friends = ["Alice", "Bob", "Charlie"]
print("Friends list:", friends)
print("Second friend:", friends[1])

# Changing element (lists are mutable)
friends[0] = "Ann"
print("Modified list:", friends)
print("")


# ==========================================================
# 3. len() and range() functions
# ==========================================================

nums = [10, 20, 30, 40]
print("Length of nums:", len(nums))

# range() creates a sequence of numbers
for i in range(5):
    print("Number from range:", i)
print("")

# Using range() for indexing a list
for i in range(len(nums)):
    print("Index", i, "-> value", nums[i])
print("")


# ==========================================================
# 4. Concatenation and slicing
# ==========================================================

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("Concatenated list:", c)

# slicing
print("Slice c[1:4]:", c[1:4])
print("Slice c[:3]:", c[:3])
print("Slice c[4:]:", c[4:])
print("")


# ==========================================================
# 5. List methods
# ==========================================================

nums = [3, 1, 4, 1, 5]
print("Original list:", nums)

nums.append(9)
print("After append:", nums)

nums.sort()
print("After sort:", nums)

print("Minimum:", min(nums))
print("Maximum:", max(nums))
print("Sum:", sum(nums))
print("Average:", sum(nums) / len(nums))
print("")


# ==========================================================
# Practice: Average from user inputs
# ==========================================================

print("=== Practice: Average using a List ===")

values = [10, 20, 30, 40, 50]  # example inputs
print("Values:", values)
print("Average =", sum(values) / len(values))
print("")


# ==========================================================
# 6. Strings and lists – split() method
# ==========================================================

print("=== Best friends: strings and lists ===")

line = "My name is Alice"
words = line.split()
print("Words:", words)
print("Number of words:", len(words))
print("Second word:", words[1])
print("")

letters = []
for letter in line:
    letters.append(letter)
print("Letters:", letters)
print("")

# Using split with custom delimiter
line2 = "apple,banana,pear"
fruits = line2.split(",")
print("Split by comma:", fruits)
print("")


# ==========================================================
# Practice: Extract email domain and month
# ==========================================================

print("=== Practice: Email header parsing ===")

header = "From professor.xman@uct.edu Sat Jan 5 09:14:16 2008"
parts = header.split()
email = parts[1]
month = parts[3]
domain = email.split("@")[1]
print("Email domain:", domain)
print("Month:", month)
print("")


# ==========================================================
# 7. Building lists dynamically using append()
# ==========================================================

print("=== Building a list from scratch ===")

numbers = []
numbers.append(3)
numbers.append(7)
numbers.append(10)
print("Numbers after appending:", numbers)
print("Length =", len(numbers))
print("")


# ==========================================================
# 8. Checking for membership: in, not in
# ==========================================================

nums = [1, 2, 3, 4, 5]
print("=== Checking membership ===")
print("2 in nums?", 2 in nums)
print("8 not in nums?", 8 not in nums)
print("")


# ==========================================================
# 9. Dictionaries – key-value collection
# ==========================================================

print("=== Dictionaries ===")

phone_book = {"Alice": "1234", "Bob": "5678"}
print("Phone book:", phone_book)
print("Alice's number:", phone_book["Alice"])

# Add a new entry
phone_book["Charlie"] = "91011"
print("After adding Charlie:", phone_book)
print("")

# Dictionaries are unordered (pre-Python 3.7 visual order)
print("'Bob' in phone_book?", "Bob" in phone_book)
print("'David' in phone_book?", "David" in phone_book)
print("")


# ==========================================================
# 10. Counting with dictionaries
# ==========================================================

print("=== Counting with a dictionary ===")

counts = {}

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1
print("Word counts:", counts)
print("")


# ==========================================================
# 11. Using get() to simplify counting pattern
# ==========================================================

print("=== Counting with get() method ===")

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("Word counts using get():", counts)
print("")


# ==========================================================
# Practice: Count words in a line using dictionary and get()
# ==========================================================

print("=== Practice: Word frequency in a line ===")

line = "Python is fun and Python is powerful"
word_list = line.split()
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)
print("")


# ==========================================================
# 12. Looping through dictionary items
# ==========================================================

print("=== Loop through dictionary items ===")

for key in word_count:
    print("Key:", key, "Value:", word_count[key])
print("")

# Using items() gives both key and value
for k, v in word_count.items():
    print("Key =", k, "Value =", v)
print("")


# ==========================================================
# 13. Tuples introduction
# ==========================================================

print("=== Tuples ===")

t = (10, 20, 30)
print("Tuple:", t)
print("First element:", t[0])

# Tuples are immutable
# t[0] = 99  # would cause an ERROR
print("Tuples cannot be modified.")
print("")


# ==========================================================
# 14. Tuples from dictionary using items()
# ==========================================================

print("=== Tuples and Dictionaries ===")

pairs = word_count.items()
print("Pairs from dictionary:", pairs)
print("List of pairs:", list(pairs))
print("")


# ==========================================================
# 15. Sorting dictionaries by key or value
# ==========================================================

print("=== Sorting dictionaries ===")

# Sort by key
print("Sorted by key:", sorted(word_count.items()))

# Sort by value using reverse pair (value, key)
print("Sorted by value:")
tmp = []
for k, v in word_count.items():
    tmp.append((v, k))
tmp.sort(reverse=True)
print(tmp)
print("")

# Extract top N items
print("Top 3 words by frequency:")
for value, key in tmp[:3]:
    print(key, "appears", value, "times")
print("")


# ==========================================================
# Bonus: Example with file content simulation
# ==========================================================
print("=== Finding 10 most common words (Simulated Example) ===")

# Simulate reading from a file
text = "to be or not to be that is the question to be or to go"
words = text.split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

List_of_tuples = []
for k, v in counts.items():
    List_of_tuples.append((v, k))

List_of_tuples.sort(reverse=True)

print("Top word frequencies:")
for value, key in List_of_tuples[:10]:
    print(key, ":", value)
print("")

# ==========================================================
print("=== End of Lecture 5 Demonstrations ===")
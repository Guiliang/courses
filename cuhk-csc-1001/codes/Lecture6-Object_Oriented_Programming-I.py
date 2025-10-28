"""
==========================================================
Lecture 6: Object-Oriented Programming
Instructor: Prof. Guiliang Liu
Reconstructed & Annotated by ChatGPT
==========================================================

Contents of this file:
 1. Object identity and type()
 2. Variables as references
 3. Class definition, self, and constructor
 4. Example: Circle class
 5. Example: TV class (mutable objects)
 6. Practice 1 – Mutable object output
 7. Hiding and protecting data with private fields
 8. Practice 2 – Private field problem and fix
 9. Function abstraction (isPrime)
10. Class abstraction and encapsulation (BMI class)
11. Practice 3 – Rectangle class
12. Practice 4 – Stock class
==========================================================
"""

# ==========================================================
# 1. Everything is an Object
# ==========================================================

print("=== 1. Object Identity and Type ===")
x = 10
y = "Python"

print("id(x):", id(x))
print("id(y):", id(y))
print("type(x):", type(x))
print("type(y):", type(y))
print("")

# ==========================================================
# 2. Variable is only a reference
# ==========================================================

print("=== 2. Variable as a Reference ===")
a = [1, 2, 3]
b = a
print("Before modification -> a:", a, "b:", b)
b.append(4)
print("After modification -> a:", a, "b:", b)
print("a and b reference same object:", a is b)
print("id(a):", id(a), "id(b):", id(b))
print("")

# ==========================================================
# 3. Defining a class, the __init__ constructor, and self
# ==========================================================

print("=== 3. Define a Basic Class: Human ===")


class Human:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age  # instance variable

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")


# Creating objects (instantiation)
person1 = Human("Alice", 20)
person2 = Human("Bob", 25)

person1.eat()
person2.sleep()
print("person1 name:", person1.name)
print("")

# ==========================================================
# 4. Circle Example (default constructor argument)
# ==========================================================

print("=== 4. Circle Class Example ===")


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def getArea(self):
        return 3.14159 * self.radius * self.radius

    def getPerimeter(self):
        return 2 * 3.14159 * self.radius


c1 = Circle()  # default radius = 1.0
c2 = Circle(3.0)  # radius = 3.0
print("Circle 1 -> radius:", c1.radius, "area:", c1.getArea())
print("Circle 2 -> radius:", c2.radius, "perimeter:", c2.getPerimeter())
print("")

# ==========================================================
# 5. Example: TV Class (mutable objects)
# ==========================================================

print("=== 5. TV Class Example ===")


class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def showStatus(self):
        if self.on:
            print("TV is ON -> channel:", self.channel, "volume:", self.volumeLevel)
        else:
            print("TV is OFF")


# Example usage
tv1 = TV()
tv1.turnOn()
tv1.setChannel(36)
tv1.setVolume(4)
tv1.showStatus()
tv1.turnOff()
tv1.showStatus()
print("")

# ==========================================================
# 6. PRACTICE 1 — Mutable Object Output
# ==========================================================

print("=== Practice 1: Mutable Object Experiment ===")
class NumberBox:
    def __init__(self, value):
        self.value = value


boxA = NumberBox(10)
boxB = boxA
print("Before change -> boxA.value =", boxA.value, ", boxB.value =", boxB.value)
boxB.value = 99
print("After change -> boxA.value =", boxA.value, ", boxB.value =", boxB.value)
print("Answer: both changed, because boxA and boxB reference the same object.\n")

# ==========================================================
# 7. Hiding Data Fields (using private attributes)
# ==========================================================

print("=== 7. Private Data Field Concept ===")


class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount

    def getBalance(self):
        return self.__balance

    def getOwner(self):
        return self.__owner


account = BankAccount("Alice", 1000)
account.deposit(200)
account.withdraw(150)
print("Account owner:", account.getOwner(), "balance:", account.getBalance())
print("")

# ==========================================================
# 8. PRACTICE 2 — Private Field Problem and Fix
# ==========================================================

print("=== Practice 2: Private Field Fix ===")


class CirclePrivate:
    def __init__(self, radius):
        self.__radius = radius  # private field

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be positive.")


# Incorrect attempt to modify private attribute
c = CirclePrivate(5)
c.__radius = 100  # creates new member, does NOT change private one
print("Illegal direct modification attempt: getRadius() still gives", c.getRadius())

# Correct fix:
c.setRadius(8)
print("After using setter, radius =", c.getRadius())
print("Answer: direct modification fails because __radius is name‑mangled; use set/get methods.\n")

# ==========================================================
# 9. Abstraction — Function Level
# ==========================================================

print("=== 9. Abstraction Example (Functions) ===")


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def printPrimeNumbers(limit):
    for num in range(2, limit + 1):
        if isPrime(num):
            print(num, end=" ")
    print("\nDone printing primes up to", limit, "\n")


printPrimeNumbers(30)

# ==========================================================
# 10. Class Abstraction & Encapsulation — BMI Example
# ==========================================================

print("=== 10. BMI Class Example ===")


class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight  # kilograms
        self.__height = height  # meters

    def getBMI(self):
        bmi = self.__weight / (self.__height ** 2)
        return bmi

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def getName(self):
        return self.__name


# Using the class
p = BMI("John", 22, 68, 1.75)
print("Name:", p.getName(), "BMI value:", p.getBMI(), "Status:", p.getStatus())
print("")

# ==========================================================
# 11. PRACTICE 3 — Rectangle Class
# ==========================================================

print("=== Practice 3: Rectangle Class ===")


class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


# Test rectangles
r1 = Rectangle()
r2 = Rectangle(4, 5)

print("Rectangle 1 -> width:", r1.width, "height:", r1.height, "area:", r1.getArea())
print("Rectangle 2 -> width:", r2.width, "height:", r2.height,
      "perimeter:", r2.getPerimeter(), "area:", r2.getArea())
print("Answer: default rectangle area 2, second rectangle area 20, perimeter 18.\n")

# ==========================================================
# 12. PRACTICE 4 — Stock Class
# ==========================================================

print("=== Practice 4: Stock Class ===")


class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    # Getters
    def getSymbol(self):
        return self.__symbol

    def getName(self):
        return self.__name

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    # Setters
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price

    def setCurrentPrice(self, price):
        self.__currentPrice = price

    # Compute change percent
    def getChangePercent(self):
        change = (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100
        return change


# Example usage
stock1 = Stock("AAPL", "Apple Inc.", 150.0, 155.5)
print("Symbol:", stock1.getSymbol(), "Name:", stock1.getName())
print("Prev:", stock1.getPreviousClosingPrice(), "Now:", stock1.getCurrentPrice())
print("Change Percent:", stock1.getChangePercent(), "%")

# Modify prices
stock1.setCurrentPrice(160.0)
print("After update -> New Change Percent:", stock1.getChangePercent(), "%")
print("Answer: positive number indicates price increase.\n")

# ==========================================================
print("=== END OF LECTURE 6 – All Examples and Practices Completed ===")

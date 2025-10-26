"""
==========================================================
Lecture 6: Object Oriented Programming
Instructor: Prof. Guiliang Liu
Reconstructed & Annotated by ChatGPT
==========================================================

This program demonstrates:
 1. Objects and classes
 2. Constructors (__init__) and self
 3. Public vs private data fields
 4. Abstraction and encapsulation
 5. Practical Example Classes:
    - Circle
    - TV
    - BMI
    - Rectangle
    - Stock
==========================================================
"""

# ==========================================================
# 1. OBJECTS AND BASIC FUNCTIONS (id() and type())
# ==========================================================

print("=== Objects and Basic Info ===")

x = 10
y = "Python"
print("id(x):", id(x))
print("type(x):", type(x))
print("id(y):", id(y))
print("type(y):", type(y))
print("")

# ==========================================================
# 2. EVERYTHING IS AN OBJECT
# ==========================================================

print("=== Everything is an Object ===")
a = [1, 2, 3]
print("List a:", a)
print("id(a):", id(a), "type(a):", type(a))
b = a  # variable is only a reference
print("b refers to same object:", b is a)
print("")

# ==========================================================
# 3. DEFINING A CLASS AND CREATING OBJECT INSTANCES
# ==========================================================

print("=== Define a Simple Class Example ===")

class Human:
    def __init__(self, name, height, weight):
        # data fields (attributes)
        self.name = name
        self.height = height
        self.weight = weight

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")

# Instantiate objects from class
person1 = Human("Alice", 165, 55)
person2 = Human("Bob", 180, 72)

person1.eat()
person2.sleep()
print("Person1 height:", person1.height)
print("")

# ==========================================================
# 4. Circle CLASS Example (constructor, methods, default)
# ==========================================================

print("=== Circle Class Example ===")

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def getArea(self):
        return 3.14159 * self.radius * self.radius

    def getPerimeter(self):
        return 2 * 3.14159 * self.radius

# create circle objects
c1 = Circle()
c2 = Circle(3)
print("Circle 1: radius =", c1.radius, "area =", c1.getArea())
print("Circle 2: radius =", c2.radius, "area =", c2.getArea(), "perimeter =", c2.getPerimeter())
print("")

# ==========================================================
# 5. TV CLASS EXAMPLE (mutable attributes)
# ==========================================================

print("=== TV Class Example ===")

class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 5
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def setChannel(self, channel):
        if self.on:
            self.channel = channel

    def setVolume(self, volume):
        if self.on:
            self.volume = volume

    def showStatus(self):
        if self.on:
            print("TV is on. Channel:", self.channel, "Volume:", self.volume)
        else:
            print("TV is off.")

# Using the TV class
tv1 = TV()
tv1.turnOn()
tv1.setChannel(7)
tv1.setVolume(10)
tv1.showStatus()
print("")


# ==========================================================
# 6. PRIVATE DATA FIELDS AND ENCAPSULATION
# ==========================================================

print("=== Private Data Fields Example ===")

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner       # private field
        self.__balance = balance   # private field

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Invalid withdrawal!")

    def getBalance(self):
        return self.__balance

    def getOwner(self):
        return self.__owner

# Example usage
account = BankAccount("Alice", 1000)
print("Owner:", account.getOwner())
print("Balance:", account.getBalance())
account.deposit(500)
account.withdraw(300)
print("Final balance:", account.getBalance())

# Cannot directly modify private data:
# account.__balance = 9999  # This will not change the true balance
print("")


# ==========================================================
# 7. ABSTRACTION EXAMPLE
# ==========================================================

print("=== Abstraction Example ===")

# Programmer 1 defines a reusable function
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Programmer 2 uses the function without caring how it's implemented
def printPrimeNumbers(limit):
    count = 0
    for i in range(2, limit + 1):
        if isPrime(i):
            print(i, end=" ")
            count = count + 1
    print("\nTotal primes:", count)

printPrimeNumbers(30)
print("")


# ==========================================================
# 8. CLASS ABSTRACTION AND ENCAPSULATION: BMI EXAMPLE
# ==========================================================

print("=== BMI Class Example ===")

class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight  # in kilograms
        self.__height = height  # in meters

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

# Using the BMI class
person = BMI("Alice", 22, 65, 1.70)
print("Name:", person.getName(), "BMI:", person.getBMI(), "Status:", person.getStatus())
print("")


# ==========================================================
# 9. PRACTICE: RECTANGLE CLASS
# ==========================================================

print("=== Practice: Rectangle Class ===")

class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

# Testing Rectangle
r1 = Rectangle()
r2 = Rectangle(4, 10)
print("Rectangle 1: width =", r1.width, "height =", r1.height, "area =", r1.getArea())
print("Rectangle 2: width =", r2.width, "height =", r2.height, "perimeter =", r2.getPerimeter())
print("")


# ==========================================================
# 10. PRACTICE: STOCK CLASS
# ==========================================================

print("=== Practice: Stock Class ===")

class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    # Get methods
    def getSymbol(self):
        return self.__symbol

    def getName(self):
        return self.__name

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    # Set methods
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price

    def setCurrentPrice(self, price):
        self.__currentPrice = price

    def getChangePercent(self):
        change = (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100
        return change

# Using the Stock class
stock = Stock("AAPL", "Apple Inc.", 150.0, 155.5)
print("Stock:", stock.getSymbol(), "-", stock.getName())
print("Previous Price:", stock.getPreviousClosingPrice())
print("Current Price:", stock.getCurrentPrice())
print("Change Percent:", stock.getChangePercent(), "%")
print("")

# ==========================================================
print("=== End of Lecture 6 Demonstrations ===")
"""
==========================================================
Lecture 7: Object-Oriented Programming II
Instructor: Prof. Guiliang Liu
Reconstructed & Annotated by ChatGPT
==========================================================

Topics:
 1. Inheritance: superclass & subclass
 2. Inheritance syntax with example
 3. Overriding methods with super()
 4. Object class and its methods (__init__, __str__, __eq__)
 5. Polymorphism and dynamic binding
 6. isinstance() function
 7. Practice questions on inheritance hierarchy
 8. Multiple inheritance
==========================================================
"""

# ==========================================================
# 1. Basic Inheritance: GeometricObject superclass
# ==========================================================

print("=== 1. Inheritance: GeometricObject Base Class ===")

class GeometricObject:
    def __init__(self, color="white", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "Color: " + self.__color + " and filled: " + str(self.__filled)

# Test GeometricObject
shape = GeometricObject("blue", True)
print("Shape from GeometricObject ->", shape)
print("")


# ==========================================================
# 2. Subclass example: Circle inherits from GeometricObject
# ==========================================================

print("=== 2. Circle Subclass Example ===")

class Circle(GeometricObject):
    def __init__(self, radius=1.0, color="white", filled=True):
        # call superclass constructor
        super().__init__(color, filled)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, r):
        self.__radius = r

    def getArea(self):
        return 3.14159 * self.__radius * self.__radius

    def getPerimeter(self):
        return 2 * 3.14159 * self.__radius

    # overriding __str__ method
    def __str__(self):
        return "Circle radius: " + str(self.__radius) + ", " + super().__str__()

# Testing Circle class
c = Circle(5, "red", False)
print(c)
print("Area:", c.getArea(), "Perimeter:", c.getPerimeter())
print("")


# ==========================================================
# 3. Rectangle Subclass Example
# ==========================================================

print("=== 3. Rectangle Subclass Example ===")

class Rectangle(GeometricObject):
    def __init__(self, width=1.0, height=1.0, color="gray", filled=True):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return "Rectangle width: " + str(self.__width) + ", height: " + str(self.__height) + ", " + super().__str__()

# Test Rectangle
r = Rectangle(4, 7, "green", True)
print(r)
print("Area:", r.getArea(), "Perimeter:", r.getPerimeter())
print("")


# ==========================================================
# 4. Demonstration: subclass vs superclass
# ==========================================================

print("=== 4. Subclass vs Superclass Relationship ===")

print("Is Circle a GeometricObject?", isinstance(c, GeometricObject))
print("Is Rectangle a GeometricObject?", isinstance(r, GeometricObject))
print("Is GeometricObject a Circle?", isinstance(shape, Circle))
print("Answer: Subclass instance IS a superclass instance, but not the reverse.\n")


# ==========================================================
# 5. Method Overriding Example & use of super()
# ==========================================================

print("=== 5. Method Overriding Demonstration ===")

class DemoParent:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Parent show() ->", self.name)

class DemoChild(DemoParent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def show(self):
        print("Child show() overrides parent. Name:", self.name, ", Age:", self.age)
        print("Now calling parent method explicitly using super():")
        super().show()

test = DemoChild("Alice", 21)
test.show()
print("Answer: subclass’ method runs first, then super().\n")


# ==========================================================
# 6. Object class by default (superclass of all)
# ==========================================================

print("=== 6. Object Class & Default Inheritance ===")

class Simple:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __str__(self):
        return "Simple object value = " + str(self.value)

a = Simple(10)
b = Simple(10)
c = Simple(20)
print(a)
print("a == b ?", a == b)
print("a == c ?", a == c)
print("Superclass of Simple:", Simple.__base__)
print("Answer: All classes inherit from object by default.\n")


# ==========================================================
# 7. Polymorphism & Dynamic Binding Example
# ==========================================================

print("=== 7. Polymorphism and Dynamic Binding ===")

def displayObject(obj):
    print(obj)
    print("Area:", obj.getArea(), "Perimeter:", obj.getPerimeter())
    # different behavior depending on instance type
    if isinstance(obj, Circle):
        print("Diameter:", obj.getRadius() * 2)
    elif isinstance(obj, Rectangle):
        # we access methods indirectly, so let's print internal properties manually
        print("Rectangle-specific info contained above.")
    print("")

# Passing subclass objects to a superclass reference
geo_list = [Circle(2, "yellow", True), Rectangle(3, 4, "cyan", False)]
for g in geo_list:
    displayObject(g)

print("Answer: dynamic binding ensures correct subclass method runs at runtime.\n")


# ==========================================================
# 8. isinstance() Practice: Fruit Hierarchy
# ==========================================================

print("=== 8. isinstance() Function Practice ===")

class Fruit:
    def eat(self):
        print("Fruit can be eaten.")

class Apple(Fruit):
    def makeAppleCider(self):
        print("Making apple cider.")

class GoldenDelicious(Apple):
    pass

class McIntosh(Apple):
    pass

class Orange(Fruit):
    def makeOrangeJuice(self):
        print("Making orange juice.")

# Instances
goldenDelicious = GoldenDelicious()
orange = Orange()

# Questions
print("(a) Is goldenDelicious instance of Fruit? ->", isinstance(goldenDelicious, Fruit))
print("(b) Is goldenDelicious instance of Orange? ->", isinstance(goldenDelicious, Orange))
print("(c) Is goldenDelicious instance of Apple? ->", isinstance(goldenDelicious, Apple))
print("(d) Is goldenDelicious instance of GoldenDelicious? ->", isinstance(goldenDelicious, GoldenDelicious))
print("(e) Is goldenDelicious instance of McIntosh? ->", isinstance(goldenDelicious, McIntosh))
print("(f) Is orange instance of Orange? ->", isinstance(orange, Orange))
print("(g) Is orange instance of Fruit? ->", isinstance(orange, Fruit))
print("(h) Is orange instance of Apple? ->", isinstance(orange, Apple))

# (i) Methods
print("(i) goldenDelicious makeAppleCider()? ->", end=" ")
goldenDelicious.makeAppleCider()   # yes
print("orange makeAppleCider()? ->", end=" ")
try:
    orange.makeAppleCider()       # will fail
except AttributeError:
    print("No, Orange cannot makeAppleCider().")

# (j) Methods
print("(j) orange makeOrangeJuice()? ->", end=" ")
orange.makeOrangeJuice()
print("goldenDelicious makeOrangeJuice()? ->", end=" ")
try:
    goldenDelicious.makeOrangeJuice()
except AttributeError:
    print("No, Apple‑derived class cannot makeOrangeJuice().")
print("Answers printed above.\n")


# ==========================================================
# 9. Another Practice: Course Class Demonstration (inheritance usage)
# ==========================================================

print("=== 9. Practice: Course Class Example ===")

class Course:
    def __init__(self, name):
        self.__name = name
        self.__students = []
    def addStudent(self, student):
        self.__students.append(student)
    def getStudents(self):
        return self.__students
    def getNumberOfStudents(self):
        return len(self.__students)
    def getCourseName(self):
        return self.__name

# Simple subclass may extend behavior
class OnlineCourse(Course):
    def __init__(self, name, platform):
        super().__init__(name)
        self.platform = platform
    def __str__(self):
        return "OnlineCourse: " + self.getCourseName() + " on " + self.platform

c1 = OnlineCourse("Programming", "edX")
c1.addStudent("Alice")
c1.addStudent("Bob")
print(c1)
print("Number of students:", c1.getNumberOfStudents())
print("")


# ==========================================================
# 10. Multiple Inheritance Example
# ==========================================================

print("=== 10. Multiple Inheritance Example ===")

class Speaker:
    def speak(self):
        print("Speaking...")

class Teacher:
    def teach(self):
        print("Teaching...")

class Lecturer(Speaker, Teacher):
    def lecture(self):
        print("Delivering lecture with both speaking and teaching skills.")

# Test multiple inheritance
lecturer = Lecturer()
lecturer.speak()
lecturer.teach()
lecturer.lecture()

print("Answer: Lecturer class inherits from both Speaker and Teacher.\n")

# ==========================================================
print("=== END OF LECTURE 7 – COMPLETE PYTHON IMPLEMENTATION ===")
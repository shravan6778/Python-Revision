'''
A variable is a named container that stores a reference to a value in memory, so it can be referenced and manipulated during program execution.
In Python, you do not declare a variable's type — you simply assign a value. The variable comes into existence the moment you assign to it.
'''
age = 22
name = "Shravan"
height = 5.11
active = True

print(age, name, height, active)

#type of any variable using type()
print(type(age))
print(type(name))

#memory address (identity) of a variable using id()
print(id(age))

'''
Python is dynamically typed — the same variable can hold different types at different times. The type is tied to the value, not the variable name.
'''
x = 10
print(f"x = {x}, type: {type(x)}")

x = "Hello"
print(f"x = {x}, type: {type(x)}")

x = 3.14
print(f"x = {x}, type: {type(x)}")

print(5 + "5") #Type error because python is strongly typed

# Valid variable names
_private   = "underscore start is fine"
snake_case = "this is the Python convention, for variables and functions"   # preferred
PascalCase = "For Classes"
CONSTANT   = "ALL_CAPS for constants by convention"
var2       = "letter first, then number is fine"

#Assign the same value to multiple variables at once
a = b = c = 100
print(a, b, c)

#Tuple unpacking — assign multiple variables in one line
x, y, z = 100, 2.0, "Hello"
print(x, y, z)

#Swap two variables — Pythonic way (no temp variable needed!)
first = 10
second = 20
first, second = second, first
print(first, second)

#Extended unpacking with * (star) — capture remaining values
head, *tail = [1, 2, 3, 4, 5]
print(head, tail)

*body, last = [1, 2, 3, 4, 5]
print(body, last)

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

#Variable Scope
global_var = "I am global - accessible everywhere"

def my_function():
    local_var = "I am local - only inside this function"
    print(global_var)
    print(local_var)
    
my_function()
print(global_var)
print(local_var) #NameError - local_var does not exist

#The LEGB Rule — Python's Scope Search Order
'''
L → Local       (inside the current function)
E → Enclosing   (inside any outer/nested function)
G → Global      (at the module/file level)
B → Built-in    (Python's built-in names: print, len, range, type...)
'''

x = "global"          # Global scope

def outer():
    x = "enclosing"   # Enclosing scope

    def inner():
        x = "local"   # Local scope
        print(x)      # Finds 'local' first — stops here

    inner()
    print(x)          # Finds 'enclosing'

outer()
print(x)              # Finds 'global'

# Output:
# local
# enclosing
# global

#Object References & Mutability
'''
In Python, variables do not store values directly — they store references (pointers) to objects in memory.

Immutable Objects (int, str, float, tuple, bool)

When you "change" an immutable variable, Python creates a new object and points the variable to it. The original object is untouched.
'''

a = 10
b = a             # b points to the SAME object as a

print(f"a: {a}, b: {b}") # a: 10, b: 10
print(id(a))
print(id(b))
print(f"Same object? {a is b}")    # True

a = 20  # a now points to a NEW object (20); b still points to 10
print(f"a: {a}, b: {b}")          # a: 20, b: 10
print(f"Same object? {a is b}")    # False

'''
Mutable Objects (list, dict, set)

When you assign one variable to another, both point to the same object. Modifying through one affects both.
'''
list_one = [1, 2, 3]
list_two = list_one    # NOT a copy — both point to the SAME list in memory

list_two.append(4)

print(f"list_one: {list_one}")              # [1, 2, 3, 4] — also changed!
print(f"list_two: {list_two}")              # [1, 2, 3, 4]
print(f"Same object? {list_one is list_two}")   # True



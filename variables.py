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


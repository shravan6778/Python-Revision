# Python Variables & Memory Management

This document serves as a comprehensive revision guide covering the fundamental concepts of variables, scoping, and memory management in Python based on the provided script.

## Topics Covered

### 1. Variable Creation & Basic Types

Variables are named containers that store references to values in memory. Python determines the type automatically when you assign a value.

- **`type(variable)`**: Returns the data type of the variable.
- **`id(variable)`**: Returns the memory address (identity) of the variable.

### 2. Dynamic vs. Strong Typing

- **Dynamically Typed**: A single variable can hold different types of data at different times. The type is tied to the actual value in memory, not the variable name itself (e.g., `x = 10` then `x = "Hello"` is perfectly valid).
- **Strongly Typed**: Python does not perform implicit type coercion for unsupported operations. For example, `5 + "5"` raises a `TypeError`.

### 3. Naming Conventions

- `snake_case`: The standard Python convention for variables and functions.
- `PascalCase`: Standard for defining Classes.
- `UPPER_CASE`: Standard for defining constants.
- `_private`: Prefixing with an underscore indicates a variable is for internal/private use.

### 4. Assignment & Unpacking

Python offers highly expressive ways to assign and swap values:

- **Chained Assignment**: `a = b = c = 100`
- **Tuple Unpacking**: `x, y, z = 100, 2.0, "Hello"`
- **Variable Swapping**: `first, second = second, first` (Achieved cleanly without a temporary variable)
- **Extended Unpacking**: Use the `*` (star) operator to pack remaining values into a list.
  - Example: `first, *middle, last = [1, 2, 3, 4, 5]` captures the middle elements dynamically.

### 5. Variable Scope & The LEGB Rule

Python resolves variable names by searching scopes in a specific order known as the **LEGB** rule:

1. **L - Local**: Inside the current function.
2. **E - Enclosing**: Inside any outer (nested) functions.
3. **G - Global**: At the top level of the module/file.
4. **B - Built-in**: Python's built-in names (e.g., `print`, `len`, `type`).

_(Note: Trying to access a local variable from a global scope will result in a `NameError`.)_

### 6. Object References & Mutability

In Python, variables do not store values directly; they store references (pointers) to objects in memory.

- **Immutable Objects** (`int`, `str`, `float`, `tuple`, `bool`):
  When you "change" an immutable variable, Python creates a completely new object in memory and updates the reference. If `b = a`, and `a` is reassigned, `b` remains completely unaffected.
- **Mutable Objects** (`list`, `dict`, `set`):
  When you assign one variable to another (e.g., `list_two = list_one`), both variables point to the exact **same object** in memory. Modifying the object through one variable (like `list_two.append(4)`) will reflect in all variables pointing to that object.

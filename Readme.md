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

---

### 7. Built-in Data Types

Python has a rich set of built-in data types to represent different kinds of data.

- **Numeric Types (`int`, `float`, `complex`)**:
- **`int` (Integers)**: Whole numbers. Supports visual separators (`999_999_999`) and different number bases: Binary (`0b1010`), Octal (`0o12`), and Hexadecimal (`0xA`).
- **`float` (Floating Point)**: Decimal numbers. Supports scientific notation (e.g., `1.5e10`). Note: Floats have inherent precision limits (e.g., `0.1 + 0.2` results in `0.30000000000000004`), so use `round()` when necessary.
- **`complex` (Complex Numbers)**: Written with a `j` suffix (e.g., `2 + 3j`). You can access parts using `.real` and `.imag`.
- _Mathematical Quirk_: Floor division (`//`) rounds toward _negative infinity_. `7 // 2` is `3`, but `-7 // 2` is `-4`.

- **Text Type (`str`)**: Strings can be defined using single quotes, double quotes, or triple quotes (for multi-line strings).
- **Boolean Type (`bool`)**: Represents truth values, strictly `True` or `False`.
- **Sequence Types (`list`, `tuple`, `range`)**:
- **`list`**: Mutable sequences (e.g., `["apple", "banana"]`).
- **`tuple`**: Immutable sequences (e.g., `(10, 20)`).
- **`range`**: Generates a sequence of numbers. Supports start, stop, and step arguments (e.g., `range(10, 0, -1)` counts backwards).

- **Set Type (`set`)**: Unordered collections of unique elements (e.g., `{1, 2, 3}`). Duplicates are removed automatically upon creation.
- **Mapping Type (`dict`)**: Key-value pairs (e.g., `{"name": "Shravan", "age": 21}`). Values can be of any data type, including lists or other dictionaries.
- **NoneType (`None`)**: A special type representing the absence of a value.

---

### 8. Type Conversion (Typecasting)

Python allows you to convert values from one data type to another, either automatically or manually.

- **Implicit Conversion**: Python does this automatically to prevent data loss. For example, adding an `int` and a `float` results in a `float` (`10 + 5.5 = 15.5`).
- **Explicit Conversion**: Doing it manually using built-in functions.
- String to Number: `int("25")` or `float("19.99")`
- Number to String: `str(98)` (or use f-strings: `f"Score: {score}"`)
- Collection Conversions: You can easily cast between collections. `set([1, 2, 2])` becomes `{1, 2}`, which can then be cast to a tuple via `tuple(my_set)`.

- **Boolean Conversions (Truthy & Falsy)**: When casting to `bool()`, Python evaluates values based on their content:
- **Falsy (Evaluates to False)**: `0`, `""` (empty string), `None`, `[]` (empty list/collections).
- **Truthy (Evaluates to True)**: Any non-zero number (e.g., `42`), non-empty strings (`"hi"`), and populated collections (`[0]`).

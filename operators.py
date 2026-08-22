#Arithmetic Operators

a, b = 20, 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# negative floor division
print(-7 // 2)
print(-7 % 2)

#Relational / Comparison Operators

m, n = 10, 20
print(m == n)
print(m != n)
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)

#chained comparisons
age = 22
print(18 <= age < 30)

#Logical Operators
#Precedence among logical operators: not > and > or

high_income = True
good_credit = False

print(high_income and good_credit)

print(high_income or good_credit)

print(not good_credit)

# Precedence demo
result = True or False and False
print(result) # True

# Short-circuit demo
def risky():
    raise ValueError("This should not run!")
print(False and risky()) # False — risky() never called
print(True or risky()) # True  — risky() never called


# Bitwise Operators
p, q = 5, 3

print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(10 << 2)
print(20 >> 2)
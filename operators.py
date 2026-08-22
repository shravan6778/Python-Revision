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

#Assignment & Augmented Operators

x = 10
x += 5
x -= 5
x *= 2
x /= 2
x //= 2
x **= 2

#Identity Operators
a = 10
b = a
c = 20
print(a is b)
print(a is not c)

#Membership Operators
l = [1, 2, 3, 4]
print(2 in l)
print(10 not in l)

# Works on strings (substring check)
email = "sandy@gmail.com"
print("@" in email)
print("gmail" in email)

# Dictionary: checks KEYS
info = {"name": "Sandy", "city": "Hyderabad"}
print("name" in info)   # True
print("Sandy" in info)  # False — "Sandy" is a value, not a key
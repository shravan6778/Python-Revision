#Python has a rich set of built-in data types. Every value in Python is an object belonging to a class.

print(type(21))
print(type(2.1))
print(type("Sandy"))
print(type(True))
print(type(2+3j))
print(type([1,2,3]))
print(type((1,2)))
print(type({1,2}))
print(type({"a":1}))
print(type(None))

#Numeric Types — int, float, complex
#int — Integer (Whole Numbers)
x = 100
y = -100
big = 999_999_999
print(type(big))

#Number bases
binary = 0b1010
octal = 0o12
hexa_dec = 0xA

print(binary, octal, hexa_dec)

#float — Floating Point (Decimal Numbers)

pi = 3.14
sci = 1.5e10    # Scientific notation: 1.5 × 10^10
print(type(pi))   
print(sci)        # 15000000000.0

# Float precision issue — important to know!
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))

# complex — Complex Numbers
c = 2 + 3j
print(type(c))
print(c.real)
print(c.imag)
print(abs(c))

#intresting floor division
print(7 // 2)   # 3
print(-7 // 2)  # -4 because floor division rounds toward negative infinity, not toward zero.

#Text Type — str
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = """Triple quotes
span multiple
lines."""

#Boolean Type — bool
is_active = True
is_logged = False

print(type(is_active))    # <class 'bool'>

#Sequence Types — list, tuple, range
fruits = ["apple", "banana", "apple", "cherry"]

coordinates = (10, 20, 30)

r1 = range(5)          
r2 = range(1, 6)       
r3 = range(0, 10, 2)   
r4 = range(10, 0, -1)  

#Set Type — set
my_set = {1, 2, 3, 3, 3, 2}   # Duplicates automatically removed
print(my_set) 

#Mapping Type — dict
student = {
    "name":     "Shravan",
    "age":      21,
    "grade":    "A",
    "subjects": ["Math", "Python", "DSA"]   # Value can be a list
}

#NoneType — None
result = None
print(result) 

#Type Conversion (Typecasting)
#Implicit Conversion — Python Does It Automatically

num_int = 10
num_float = 5.5
result = num_int + num_float
print(result)
print(type(result))

#Explicit Conversion — Doing It Manually
# str → int / float
age_str   = "25"
price_str = "19.99"

age_int     = int(age_str)       
price_float = float(price_str)   

print(age_int + 1)        
print(price_float * 2)    

# int/float → str
score   = 98
print("Score: " + str(score))          
print(f"Score: {score}") 

# bool conversions 
print(bool(0))      
print(bool(42)) 
print(bool("")) 
print(bool("hi"))
print(bool(None)) 
print(bool([]))   
print(bool([0]))   


# Collection conversions
original = [1, 2, 2, 3, 4, 4]
as_set   = set(original)     
as_tuple = tuple(as_set)     
as_list  = list(as_tuple)    
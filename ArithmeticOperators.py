#addition
a = 7
b = 3
c = a + b
print(c)

#incrementing/decrementing variables using the +=operator (works the same for -=)
a = 0
b = 0
a = a + 1
b += 1
print(a)
print(b)

a = 10
b = 3
a -= b
print(a)

#typecasting is when you change the data type of a variable
a = 3
print(type(a))
a = str(a)
print(type(a))

#string concatenation 1
a = "This is an "
b = "example string"
c = a + b
print(c)

#string concatenation 2
a = "This is an "
b = "example string"
a += b
print(a)

#division (will always produce a float)
a = 25
b = 5
print(a / b)

#floor division (does not round up or down)
a = 5
b = 2
print(a // b)

#multiplication
a = 5
b = 10
print(a * b)

#multiplication and strings (print hello hello hello)
a = 3
b = "Hello!"
print(a * b)

#powers
a = 2 ** 2
print(a)

#sqaure root
square_root = 4 ** 0.5
print(square_root)

#python uses PEMDAS for the order of operators:
#Parentheses
#Exponents
#Multiplication & Division
#Addition & Subtraction

#Modulo is the mathematical operation that performs division but returns the remainder.
modulo = 5 % 2
print(modulo)

#A compound conditional is a conditional (an if statement) that has more than one boolean expression.
if 5 < 10 and 5 > 0:
  print("True")

#compund conditional statement
num = 16

if num % 2 == 0 and num > 10:
    print("Even and greater than 10")

#example 1 - both print '19'
my_var = 19

if my_var > 15:
    if my_var < 20:
        print(my_var)

if my_var > 15 and my_var < 20:
    print(my_var)

#example 2
if True or True:
    print("Hello World")

#example 1
a = 20

if a < 10:
    print(str(a) + " is less than 10")
elif a < 20:
    print(str(a) + " is less than 20")
elif a < 30:
    print(str(a) + " is less than 30")
else:
    print(str(a) + " is greater than 30")

#example 2 - elif is for efficiency
grade = 65

if grade < 60:
    print("You got an F.")
elif grade < 70:
    print("You got a D.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

#example 3
my_var = 2
if my_var < 5:
    print("Less than 5.")
elif my_var <= 10:
    print("Between 5 and 10.")
else:
    print("Greater than 10.")

#example 4
if my_var == 1:
    print("my_var is 1")
elif my_var == 2:
    print("my_var is 2")
else:
    print("my_var is greater than 2")

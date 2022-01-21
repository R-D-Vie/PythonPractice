#syntax
if 4 > 6:
  print("The boolean expression is true")
else:
  print("The boolean expression is false")

#example1
my_bool = True

if my_bool:
    print("The value of my_bool is true")
else:
    print("The value of my_bool is false")


#example2
num = -8

if num % 2 == 0:
    print(str(num) + " is an even number")
else:
    print(str(num) + " is an odd number")

#complex example - nesting if-else statements
my_var=rainy

if rainy:
    if windy:
        print("Wear a rain jacket.")
    else:
        print("Bring an umbrella!")
else:
    if cold:
        print("You might need a coat.")
    else:
        print("Enjoy your day!")
